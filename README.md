# Stonfi API Client Library

This library provides a Python interface for interacting with the Stonfi DEX API. It allows you to retrieve information about assets, farms, pools, markets, and wallets, as well as simulate and execute swaps.

## Practical Usage
Examples
The following `examples` are included in this repository:

* getting_assets_on_wallet.py: Gets the assets on a specified wallet address.
* describe_asset.py: Describes a specified asset.
* describe_farm.py: Describes a specified farm.
* describe_pool.py: Describes a specified pool.
* simulating_progressive.py: Simulates a progressive transaction.
* timechecking_dex_activity.py: Checks the DEX activity for a specified period of time.
* top4_remaining_pools.py: Gets the top 4 remaining pools.

## Usage

Here's an example of how to use the library to retrieve information about an asset:
NOTICE! You need to add timeout= optional kwarg if you are going to use queries with huge selection.
```python
from stonfi import APIClient

async def main():
    client = APIClient()  # you need to add timeout= optional kwarg if you are going to use queries with huge selection
    asset = await client.get_asset("EQDwlPXvgDemNYEjEaJw8vxh9bYPqC--w2NnqFryU6Ae6Eoz")
    print(asset.name)

asyncio.run(main())
```

The library provides the following methods for interacting with the Stonfi API:

* `get_assets()`: Retrieve a list of all assets on the DEX.
* `get_asset(asset_id)`: Retrieve information about a specific asset.
* `get_farms()`: Retrieve a list of all farms on the DEX.
* `get_farm(farm_id)`: Retrieve information about a specific farm.
* `get_markets()`: Retrieve a list of all markets on the DEX.
* `get_pool(pool_id)`: Retrieve information about a specific pool.
* `get_swap_status(contract_id, offer_id, units)`: Retrieve the status of a swap between two assets.
* `reverse_swap_simulate(simulate_data)`: Simulate a reverse swap between two assets.
* `swap_simulate(simulate_data)`: Simulate a swap between two assets.
* `get_jetton_address(jetton_master_id, jetton_id)`: Retrieve the address of a jetton.
* `get_wallet_assets(wallet_id)`: Retrieve a list of all assets in a specific wallet.
* `get_wallet_asset(wallet_id, asset_id)`: Retrieve information about a specific asset in a specific wallet.
* `get_wallet_farms(wallet_id)`: Retrieve a list of all farms in a specific wallet.
* `get_wallet_farm(wallet_id, farm_id)`: Retrieve information about a specific farm in a specific wallet.
* `get_wallet_operations(wallet_id, since, until)`: Retrieve a list of all operations in a specific wallet within a specific time range.
* `get_wallet_pools(wallet_id)`: Retrieve a list of all pools in a specific wallet.
* `get_wallet_pool(wallet_id, pool_id)`: Retrieve information about a specific pool in a specific wallet.

## Composition

The library is composed of the following modules:

* `stonfi.client`: Contains the `APIClient` class, which provides the main interface for interacting with the Stonfi API.
* `stonfi.types`: Contains the data types used by the library, such as `Asset`, `Farm`, `Pool`, `SwapSimulateData`, `SwapResponse`, `SwapStatus`, and `Operation`.
* `stonfi.utils`: Contains utility functions used by the library, such as `hex_to_int` and `int_to_hex`.

## Contributing

Contributions to the library are welcome! If you find a bug or have a suggestion for a new feature, please open an issue or submit a pull request.

## License

The library is licensed under the MIT License. See the `LICENSE` file for more information.
