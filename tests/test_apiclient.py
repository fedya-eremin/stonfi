import pytest
from stonfi import APIClient
from stonfi.types import Asset, Farm, Pool, SwapSimulateData, SwapResponse, SwapStatus, Operation

ASSET_ADDR = "EQD8TJ8xEWB1SpnRE4d89YO3jl0W0EiBnNS4IBaHaUmdfizE"
CONTRACT_ADDR = "EQB3ncyBUTjZUA5EnFKR5_EnOMI9V1tTEAAPaiU71gc4TiUt"
POOL_ADDR = "EQDMN87j_dg9BGVbtEfBHxjyQE3jNgnJnRgPtnWgXE1iOr_E"
TOKEN_ADDR = "EQBynBO23ywHy_CgarY9NK9FTz0yDsG82PtcbSTQgGoXwiuA"
JETTON_ADDR = "EQCM3B12QK1e4yZSf8GtBRT0aLMNyEsBc_DhVfRRtOEffLez"
WALLET_ADDR = "EQDYzZmfsrGzhObKJUw4gzdeIxEai3jAFbiGKGwxvxHinaPP"
FARM_ADDR = "EQDEy0W_ghj7Hho2zIm0sTMTppDowUzCQCp59AY_YgAQWIPC"

@pytest.mark.asyncio
async def test_get_assets():
    client = APIClient()
    assets = await client.get_assets()
    assert isinstance(assets, list)
    assert all(isinstance(asset, Asset) for asset in assets)

@pytest.mark.asyncio
async def test_get_asset():
    client = APIClient()
    asset = await client.get_asset("EQDwlPXvgDemNYEjEaJw8vxh9bYPqC--w2NnqFryU6Ae6Eoz")
    assert isinstance(asset, Asset)

@pytest.mark.asyncio
async def test_get_farms():
    client = APIClient()
    farms = await client.get_farms()
    assert isinstance(farms, list)
    assert all(isinstance(farm, Farm) for farm in farms)

@pytest.mark.asyncio
async def test_get_farm():
    client = APIClient()
    farm = await client.get_farm(FARM_ADDR)
    assert isinstance(farm, Farm)

@pytest.mark.asyncio
async def test_get_markets():
    client = APIClient()
    markets = await client.get_markets()
    assert isinstance(markets, list)

@pytest.mark.asyncio
async def test_get_pools():
    client = APIClient()
    pools = await client.get_pools()
    assert isinstance(pools, list)
    assert all(isinstance(pool, Pool) for pool in pools)

@pytest.mark.asyncio
async def test_get_pool():
    client = APIClient()
    pool = await client.get_pool(POOL_ADDR)
    assert isinstance(pool, Pool)

@pytest.mark.asyncio
async def test_get_swap_status():
    client = APIClient()
    status = await client.get_swap_status(CONTRACT_ADDR, CONTRACT_ADDR, 1)
    assert isinstance(status, SwapStatus)

@pytest.mark.asyncio
async def test_reverse_swap_simulate():
    client = APIClient()
    simulate_data = SwapSimulateData(
        offer_address=TOKEN_ADDR,
        ask_address="EQCM3B12QK1e4yZSf8GtBRT0aLMNyEsBc_DhVfRRtOEffLez",
        units="100",
        slippage_tolerance="0.01"
    )
    response = await client.reverse_swap_simulate(simulate_data)
    assert isinstance(response, SwapResponse)

@pytest.mark.asyncio
async def test_swap_simulate():
    client = APIClient()
    simulate_data = SwapSimulateData(
        offer_address=TOKEN_ADDR,
        ask_address="EQCM3B12QK1e4yZSf8GtBRT0aLMNyEsBc_DhVfRRtOEffLez",
        units="100",
        slippage_tolerance="0.01"
    )
    response = await client.swap_simulate(simulate_data)
    assert isinstance(response, SwapResponse)

@pytest.mark.asyncio
async def test_get_jetton_address():
    client = APIClient()
    address = await client.get_jetton_address(JETTON_ADDR, JETTON_ADDR)
    assert isinstance(address, str)

@pytest.mark.asyncio
async def test_get_wallet_assets():
    client = APIClient()
    assets = await client.get_wallet_assets(WALLET_ADDR)
    assert isinstance(assets, list)
    assert all(isinstance(asset, Asset) for asset in assets)

@pytest.mark.asyncio
async def test_get_wallet_asset():
    client = APIClient()
    asset = await client.get_wallet_asset(WALLET_ADDR, "EQDwlPXvgDemNYEjEaJw8vxh9bYPqC--w2NnqFryU6Ae6Eoz")
    assert isinstance(asset, Asset)

@pytest.mark.asyncio
async def test_get_wallet_farms():
    client = APIClient()
    farms = await client.get_wallet_farms(WALLET_ADDR)
    assert isinstance(farms, list)
    assert all(isinstance(farm, Farm) for farm in farms)

@pytest.mark.asyncio
async def test_get_wallet_farm():
    client = APIClient()
    farm = await client.get_wallet_farm(WALLET_ADDR, FARM_ADDR)
    assert isinstance(farm, Farm)

@pytest.mark.asyncio
async def test_get_wallet_operations():
    client = APIClient()
    since = "2023-01-01T00:00:00"
    until = "2023-01-01T01:00:00"
    operations = await client.get_wallet_operations(WALLET_ADDR, since, until)
    assert isinstance(operations, list)
    assert all(isinstance(operation, Operation) for operation in operations)

@pytest.mark.asyncio
async def test_get_wallet_pools():
    client = APIClient()
    pools = await client.get_wallet_pools(WALLET_ADDR)
    assert isinstance(pools, list)
    assert all(isinstance(pool, Pool) for pool in pools)

@pytest.mark.asyncio
async def test_get_wallet_pool():
    client = APIClient()
    pool = await client.get_wallet_pool(WALLET_ADDR,POOL_ADDR)
    assert isinstance(pool, Pool)

