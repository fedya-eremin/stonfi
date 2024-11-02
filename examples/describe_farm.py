from stonfi import APIClient
import asyncio

async def main():
    client = APIClient()
    farm = await client.get_farm("EQDEy0W_ghj7Hho2zIm0sTMTppDowUzCQCp59AY_YgAQWIPC")

    print(f"Locked Total LP: {farm.locked_total_lp}")
    print(f"Min Stake Duration (s): {farm.min_stake_duration_s}")
    print(f"Minter Address: {farm.minter_address}")
    print(f"Pool Address: {farm.pool_address}")
    print(f"Reward Token Address: {farm.reward_token_address}")
    print(f"Status: {farm.status}")
    print(f"APY: {farm.apy}")
    print(f"Locked Total LP USD: {farm.locked_total_lp_usd}")

    print("\nRewards:")
    for reward in farm.rewards:
        print(f"  Address: {reward.address}")
        print(f"  Remaining Rewards: {reward.remaining_rewards}")
        print(f"  Reward Rate 24h: {reward.reward_rate_24h}")
        print(f"  Status: {reward.status}")
        print()

if __name__ == '__main__':
    asyncio.run(main())
