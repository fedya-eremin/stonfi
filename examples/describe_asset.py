from stonfi import APIClient
import asyncio

async def main():
    client = APIClient()
    asset_info = await client.get_asset("EQDwlPXvgDemNYEjEaJw8vxh9bYPqC--w2NnqFryU6Ae6Eoz")
    
    tags = asset_info.tags
    classification = {
        'liquidity': 'no_liquidity' in tags,
        'blacklisted': asset_info.blacklisted,
        'community': asset_info.community,
        'deprecated': asset_info.deprecated,
        'taxable': asset_info.taxable,
        'default_symbol': asset_info.default_symbol
    }

    print(f"Asset Name: {asset_info.display_name}")
    print(f"Symbol: {asset_info.symbol}")
    print(f"Contract Address: {asset_info.contract_address}")
    print(f"Classification: {classification}")

if __name__ == '__main__':
    asyncio.run(main())
