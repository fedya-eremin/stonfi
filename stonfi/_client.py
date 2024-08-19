import httpx
from stonfi.types import Asset, Farm, Pool, SwapSimulateData, SwapResponse, SwapStatus, Operation, DexStats, PoolStats


def clean_dict(d: dict) -> dict:
    return {k: v for k, v in d.items() if v is not None}


# DEX
class APIClient:
    
    def __init__(self):
        self.client = httpx.AsyncClient(transport=httpx.AsyncHTTPTransport(retries=5))

    @property
    def base_url(self):
        return "https://api.ston.fi"

    async def get_assets(self) -> list[Asset]:
        response = await self.client.get(f'{self.base_url}/v1/assets')
        return [Asset(**asset) for asset in response.json()["asset_list"]]

    async def get_asset(self, addr) -> Asset:
        response = await self.client.get(f'{self.base_url}/v1/assets/{addr}')
        return Asset(**response.json()["asset"])

    async def get_farms(self) -> list[Farm]:
        response = await self.client.get(f'{self.base_url}/v1/farms')
        return [Farm.from_dict(farm) for farm in response.json()["farm_list"]]  # type: ignore

    async def get_farm(self, farm_addr: str) -> Farm:
        response = await self.client.get(f'{self.base_url}/v1/farms/{farm_addr}')
        return Farm.from_dict(response.json()["farm"])  # type: ignore

    async def get_farms_by_pool(self, pool_addr: str) -> list[Farm]:
        response = await self.client.get(f'{self.base_url}/v1/farms_by_pool/{pool_addr}')
        return [Farm.from_dict(farm) for farm in response.json()["farm_list"]]  # type: ignore

    async def get_markets(self) -> list[list[str]]:
        response = await self.client.get(f'{self.base_url}/v1/markets')
        return response.json()["pairs"]

    async def get_pools(self) -> list[Pool]:
        response = await self.client.get(f'{self.base_url}/v1/pools')
        return [Pool.from_dict(pool) for pool in response.json()["pool_list"]]  # type: ignore

    async def get_pool(self, pool_addr: str) -> Pool:
        response = await self.client.get(f'{self.base_url}/v1/pools/{pool_addr}')
        return Pool.from_dict(response.json()["pool"])  # type: ignore

    async def get_swap_status(self, router_addr: str, owner_addr: str, query_id: int) -> SwapStatus:
        response = await self.client.get(
            f'{self.base_url}/v1/swap/status',
            params={
                "router_address": router_addr,
                "owner_address": owner_addr,
                "query_id": str(query_id)
            }
        )
        return SwapStatus.from_dict(response.json())  # type: ignore

    async def reverse_swap_simulate(self, simulate_data: SwapSimulateData) -> SwapResponse:
        url = f'{self.base_url}/v1/reverse_swap/simulate'
        response = await self.client.post(url, params=clean_dict(simulate_data.to_dict()))  # type: ignore
        return SwapResponse.from_dict(response.json())  # type: ignore

    async def swap_simulate(self, simulate_data: SwapSimulateData) -> SwapResponse:
        url = f'{self.base_url}/v1/swap/simulate'
        response = await self.client.post(url, params=clean_dict(simulate_data.to_dict()))  # type: ignore
        return SwapResponse.from_dict(response.json())  # type: ignore

    async def get_jetton_address(self, owner_addr: str, jetton_addr: str) -> str:
        url = f"{self.base_url}/v1/jetton/{jetton_addr}/address"
        params = {"owner_address": owner_addr, "addr_str": jetton_addr}
        response = await self.client.get(url, params=params)
        return response.json()["address"]

    async def get_wallet_assets(self, wallet_addr):
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/assets"
        response = await self.client.get(url)
        return [Asset(**asset) for asset in response.json()["asset_list"]]

    async def get_wallet_asset(self, wallet_addr: str, asset_addr: str):
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/assets/{asset_addr}"
        response = await self.client.get(url)
        return Asset(**response.json()["asset"])

    async def get_wallet_farms(self, addr: str) -> list[Farm]:
        url = f"{self.base_url}/v1/wallets/{addr}/farms"
        response = await self.client.get(url)
        return [Farm.from_dict(farm) for farm in response.json()["farm_list"]]  # type: ignore

    async def get_wallet_farm(self, wallet_addr: str, farm_addr: str) -> Farm:
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/farms/{farm_addr}"
        response = await self.client.get(url)
        return Farm.from_dict(response.json()["farm"])  # type: ignore

    async def get_wallet_operations(self, wallet_addr: str, since: str, until: str, op_type: str | None = None) -> list[Operation]:
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/operations"
        params = {
            "since": since,
            "until": until,
            "op_type": op_type
        }
        response = await self.client.get(url, params=clean_dict(params))
        return [Operation.from_dict(operation) for operation in response.json()["operations"]]  # type: ignore

    async def get_wallet_pools(self, wallet_addr: str) -> list[Pool]:
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/pools"
        response = await self.client.get(url)
        return [Pool.from_dict(pool) for pool in response.json()["pool_list"]]  # type: ignore

    async def get_wallet_pool(self, wallet_addr: str, pool_addr: str) -> Pool:
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/pools/{pool_addr}"
        response = await self.client.get(url)
        return Pool.from_dict(response.json()["pool"])  # type: ignore

    async def get_dex_stats(self, since: str, until: str) -> DexStats:
        url = f"{self.base_url}/v1/stats/dex"
        params = {"since": since, "until": until}
        response = await self.client.get(url, params=params)
        return DexStats.from_dict(response.json()["stats"])  # type: ignore

    async def get_operations_stats(self, since, until) -> list[Operation]:
        url = f"{self.base_url}/v1/stats/operations"
        params = {"since": since, "until": until}
        response = await self.client.get(url, params=params)
        return [Operation.from_dict(operation) for operation in response.json()["operations"]]  # type: ignore

    async def get_pool_stats(self, since: str, until: str) -> PoolStats:
        url = f"{self.base_url}/v1/stats/pool"
        params = {"since": since, "until": until}
        response = await self.client.get(url, params=params)
        return [PoolStats.from_dict(stat) for stat in response.json()["stats"]]  # type: ignore


    async def close(self):
        await self.client.aclose()
