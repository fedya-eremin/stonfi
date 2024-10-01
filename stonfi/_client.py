import httpx
from stonfi.types import Asset, Farm, Pool, SwapSimulateData, SwapResponse, SwapStatus, Operation, DexStats, PoolStats


def clean_dict(d: dict) -> dict:
    """
    Filter out None values from a dictionary.

    Args:
        d (dict): The input dictionary to clean.

    Returns:
        dict: A new dictionary containing only the key-value pairs from `d`
              where the value is not None.
    """
    return {k: v for k, v in d.items() if v is not None}


class APIClient:
    """
    A client for interacting with the STON.fi API using asynchronous HTTP requests.
    
    Attributes:
        client (httpx.AsyncClient): The HTTP client used to make requests to the API.
    """

    def __init__(self, timeout: float = 15):
        """
        Initializes the APIClient with a default AsyncClient that retries up to 5 times
        in case of failures.
        """
        self.client = httpx.AsyncClient(
            transport=httpx.AsyncHTTPTransport(retries=5),
            timeout=timeout,
        )

    @property
    def base_url(self) -> str:
        """
        Returns the base URL for the API.
        
        Returns:
            str: The base URL for the STON.fi API.
        """
        return "https://api.ston.fi"

    async def get_assets(self) -> list[Asset]:
        """
        Fetches a list of all assets available in the API.
        
        Returns:
            list[Asset]: A list of Asset objects representing all assets.
        """
        response = await self.client.get(f'{self.base_url}/v1/assets')
        return [Asset(**asset) for asset in response.json()["asset_list"]]

    async def get_asset(self, addr: str) -> Asset:
        """
        Fetches details of a specific asset by its address.
        
        Args:
            addr (str): The address of the asset.
        
        Returns:
            Asset: An Asset object representing the asset.
        """
        response = await self.client.get(f'{self.base_url}/v1/assets/{addr}')
        return Asset(**response.json()["asset"])

    async def get_farms(self) -> list[Farm]:
        """
        Fetches a list of all farms available in the API.
        
        Returns:
            list[Farm]: A list of Farm objects representing all farms.
        """
        response = await self.client.get(f'{self.base_url}/v1/farms')
        return [Farm.from_dict(farm) for farm in response.json()["farm_list"]]

    async def get_farm(self, farm_addr: str) -> Farm:
        """
        Fetches details of a specific farm by its address.
        
        Args:
            farm_addr (str): The address of the farm.
        
        Returns:
            Farm: A Farm object representing the farm.
        """
        response = await self.client.get(f'{self.base_url}/v1/farms/{farm_addr}')
        return Farm.from_dict(response.json()["farm"])

    async def get_farms_by_pool(self, pool_addr: str) -> list[Farm]:
        """
        Fetches a list of farms associated with a specific pool address.
        
        Args:
            pool_addr (str): The address of the pool.
        
        Returns:
            list[Farm]: A list of Farm objects associated with the pool.
        """
        response = await self.client.get(f'{self.base_url}/v1/farms_by_pool/{pool_addr}')
        return [Farm.from_dict(farm) for farm in response.json()["farm_list"]]

    async def get_markets(self) -> list[list[str]]:
        """
        Fetches a list of trading pairs available in the market.
        
        Returns:
            list[list[str]]: A list of trading pairs, where each pair is represented by a list of strings.
        """
        response = await self.client.get(f'{self.base_url}/v1/markets')
        return response.json()["pairs"]

    async def get_pool(self, pool_addr: str) -> Pool:
        """
        Fetches details of a specific pool by its address.
        
        Args:
            pool_addr (str): The address of the pool.
        
        Returns:
            Pool: A Pool object representing the pool.
        """
        response = await self.client.get(f'{self.base_url}/v1/pools/{pool_addr}')
        return Pool.from_dict(response.json()["pool"])

    async def get_swap_status(self, router_addr: str, owner_addr: str, query_id: int) -> SwapStatus:
        """
        Fetches the status of a specific swap operation.
        
        Args:
            router_addr (str): The address of the router.
            owner_addr (str): The address of the owner.
            query_id (int): The query ID for the swap operation.
        
        Returns:
            SwapStatus: A SwapStatus object representing the status of the swap.
        """
        response = await self.client.get(
            f'{self.base_url}/v1/swap/status',
            params={
                "router_address": router_addr,
                "owner_address": owner_addr,
                "query_id": str(query_id)
            }
        )
        return SwapStatus.from_dict(response.json())

    async def reverse_swap_simulate(self, simulate_data: SwapSimulateData) -> SwapResponse:
        """
        Simulates a reverse swap operation.
        
        Args:
            simulate_data (SwapSimulateData): The data required to simulate the reverse swap.
        
        Returns:
            SwapResponse: A SwapResponse object representing the result of the simulation.
        """
        url = f'{self.base_url}/v1/reverse_swap/simulate'
        response = await self.client.post(url, params=clean_dict(simulate_data.to_dict()))
        return SwapResponse.from_dict(response.json())

    async def swap_simulate(self, simulate_data: SwapSimulateData) -> SwapResponse:
        """
        Simulates a swap operation.
        
        Args:
            simulate_data (SwapSimulateData): The data required to simulate the swap.
        
        Returns:
            SwapResponse: A SwapResponse object representing the result of the simulation.
        """
        url = f'{self.base_url}/v1/swap/simulate'
        response = await self.client.post(url, params=clean_dict(simulate_data.to_dict()))
        return SwapResponse.from_dict(response.json())

    async def get_jetton_address(self, owner_addr: str, jetton_addr: str) -> str:
        """
        Fetches the jetton address for a given owner and jetton.
        
        Args:
            owner_addr (str): The owner's address.
            jetton_addr (str): The jetton's address.
        
        Returns:
            str: The jetton address.
        """
        url = f"{self.base_url}/v1/jetton/{jetton_addr}/address"
        params = {"owner_address": owner_addr, "addr_str": jetton_addr}
        response = await self.client.get(url, params=params)
        return response.json()["address"]

    async def get_wallet_assets(self, wallet_addr: str) -> list[Asset]:
        """
        Fetches the list of assets held by a specific wallet.
        
        Args:
            wallet_addr (str): The wallet's address.
        
        Returns:
            list[Asset]: A list of Asset objects representing the wallet's assets.
        """
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/assets"
        response = await self.client.get(url)
        return [Asset(**asset) for asset in response.json()["asset_list"]]

    async def get_wallet_asset(self, wallet_addr: str, asset_addr: str) -> Asset:
        """
        Fetches details of a specific asset held by a wallet.
        
        Args:
            wallet_addr (str): The wallet's address.
            asset_addr (str): The address of the asset.
        
        Returns:
            Asset: An Asset object representing the asset.
        """
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/assets/{asset_addr}"
        response = await self.client.get(url)
        return Asset(**response.json()["asset"])

    async def get_wallet_farms(self, addr: str) -> list[Farm]:
        """
        Fetches the list of farms associated with a specific wallet.
        
        Args:
            addr (str): The wallet's address.
        
        Returns:
            list[Farm]: A list of Farm objects representing the wallet's farms.
        """
        url = f"{self.base_url}/v1/wallets/{addr}/farms"
        response = await self.client.get(url)
        return [Farm.from_dict(farm) for farm in response.json()["farm_list"]]

    async def get_wallet_farm(self, wallet_addr: str, farm_addr: str) -> Farm:
        """
        Fetches details of a specific farm associated with a wallet.
        
        Args:
            wallet_addr (str): The wallet's address.
            farm_addr (str): The address of the farm.
        
        Returns:
            Farm: A Farm object representing the farm.
        """
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/farms/{farm_addr}"
        response = await self.client.get(url)
        return Farm.from_dict(response.json()["farm"])

    async def get_wallet_operations(self, wallet_addr: str, since: str, until: str, op_type: str | None = None) -> list[Operation]:
        """
        Fetches the list of operations associated with a specific wallet.
        
        Args:
            wallet_addr (str): The wallet's address.
            since (str): The start date for fetching operations (ISO 8601 format).
            until (str): The end date for fetching operations (ISO 8601 format).
            op_type (str, optional): The type of operations to fetch. Defaults to None.
        
        Returns:
            list[Operation]: A list of Operation objects representing the wallet's operations.
        """
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/operations"
        params = {
            "since": since,
            "until": until,
            "op_type": op_type
        }
        response = await self.client.get(url, params=clean_dict(params))
        return [Operation.from_dict(operation) for operation in response.json()["operations"]]

    async def get_wallet_pools(self, wallet_addr: str) -> list[Pool]:
        """
        Fetches the list of pools associated with a specific wallet.
        
        Args:
            wallet_addr (str): The wallet's address.
        
        Returns:
            list[Pool]: A list of Pool objects representing the wallet's pools.
        """
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/pools"
        response = await self.client.get(url)
        return [Pool.from_dict(pool) for pool in response.json()["pool_list"]]

    async def get_wallet_pool(self, wallet_addr: str, pool_addr: str) -> Pool:
        """
        Fetches details of a specific pool associated with a wallet.
        
        Args:
            wallet_addr (str): The wallet's address.
            pool_addr (str): The address of the pool.
        
        Returns:
            Pool: A Pool object representing the pool.
        """
        url = f"{self.base_url}/v1/wallets/{wallet_addr}/pools/{pool_addr}"
        response = await self.client.get(url)
        return Pool.from_dict(response.json()["pool"])

    async def get_dex_stats(self, since: str, until: str) -> DexStats:
        """
        Fetches DEX statistics for a given time period.
        
        Args:
            since (str): The start date for fetching DEX statistics (ISO 8601 format).
            until (str): The end date for fetching DEX statistics (ISO 8601 format).
        
        Returns:
            DexStats: A DexStats object representing the DEX statistics.
        """
        url = f"{self.base_url}/v1/stats/dex"
        params = {"since": since, "until": until}
        response = await self.client.get(url, params=params)
        return DexStats.from_dict(response.json()["stats"])

    async def get_operations_stats(self, since: str, until: str) -> list[Operation]:
        """
        Fetches operation statistics for a given time period.
        
        Args:
            since (str): The start date for fetching operation statistics (ISO 8601 format).
            until (str): The end date for fetching operation statistics (ISO 8601 format).
        
        Returns:
            list[Operation]: A list of Operation objects representing the statistics.
        """
        url = f"{self.base_url}/v1/stats/operations"
        params = {"since": since, "until": until}
        response = await self.client.get(url, params=params)
        return [Operation.from_dict(operation) for operation in response.json()["operations"]]

    async def get_pool_stats(self, since: str, until: str) -> list[PoolStats]:
        """
        Fetches pool statistics for a given time period.
        
        Args:
            since (str): The start date for fetching pool statistics (ISO 8601 format).
            until (str): The end date for fetching pool statistics (ISO 8601 format).
        
        Returns:
            list[PoolStats]: A list of PoolStats objects representing the statistics.
        """
        url = f"{self.base_url}/v1/stats/pool"
        params = {"since": since, "until": until}
        response = await self.client.get(url, params=params)
        return [PoolStats.from_dict(stat) for stat in response.json()["stats"]]

    async def close(self):
        """
        Closes the HTTP client session.
        """
        await self.client.aclose()
