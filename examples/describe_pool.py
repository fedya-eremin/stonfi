from stonfi import APIClient
import asyncio

async def main():
    client = APIClient()
    pool = await client.get_pool("EQDMN87j_dg9BGVbtEfBHxjyQE3jNgnJnRgPtnWgXE1iOr_E")

    print(f"Address: {pool.address}")
    print(f"APY 1d: {pool.apy_1d}")
    print(f"APY 7d: {pool.apy_7d}")
    print(f"APY 30d: {pool.apy_30d}")
    print(f"Collected Token0 Protocol Fee: {pool.collected_token0_protocol_fee}")
    print(f"Collected Token1 Protocol Fee: {pool.collected_token1_protocol_fee}")
    print(f"Deprecated: {pool.deprecated}")
    print(f"LP Account Address: {pool.lp_account_address}")
    print(f"LP Balance: {pool.lp_balance}")
    print(f"LP Fee: {pool.lp_fee}")
    print(f"LP Price USD: {pool.lp_price_usd}")
    print(f"LP Total Supply: {pool.lp_total_supply}")
    print(f"LP Total Supply USD: {pool.lp_total_supply_usd}")
    print(f"LP Wallet Address: {pool.lp_wallet_address}")
    print(f"Protocol Fee: {pool.protocol_fee}")
    print(f"Protocol Fee Address: {pool.protocol_fee_address}")
    print(f"Ref Fee: {pool.ref_fee}")
    print(f"Reserve0: {pool.reserve0}")
    print(f"Reserve1: {pool.reserve1}")
    print(f"Router Address: {pool.router_address}")
    print(f"Token0 Address: {pool.token0_address}")
    print(f"Token0 Balance: {pool.token0_balance}")
    print(f"Token1 Address: {pool.token1_address}")
    print(f"Token1 Balance: {pool.token1_balance}")

if __name__ == '__main__':
    asyncio.run(main())
