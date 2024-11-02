import asyncio
import matplotlib.pyplot as plt
from stonfi import APIClient
from stonfi.types import SwapSimulateData

async def simulate_swap(client, offer_address, ask_address, units, slippage_tolerance):
    swap_result = await client.swap_simulate(SwapSimulateData(
        offer_address=offer_address,
        ask_address=ask_address,
        units=units,
        slippage_tolerance=slippage_tolerance
    ))
    return swap_result

async def plot_swap_results(results, units_list):
    received_units = [result['received_units'] for result in results]
    plt.figure(figsize=(10, 5))
    plt.plot(units_list, received_units, marker='o', linestyle='-', color='b')
    plt.xlabel('Offered Units')
    plt.ylabel('Received Units')
    plt.title('Swap Simulation Results')
    plt.grid(True)
    plt.show()

async def main():
    client = APIClient()

    offer_address = "EQBynBO23ywHy_CgarY9NK9FTz0yDsG82PtcbSTQgGoXwiuA"
    ask_address = "EQCM3B12QK1e4yZSf8GtBRT0aLMNyEsBc_DhVfRRtOEffLez"
    slippage_tolerance = "0.01"

    units_list = [50, 100, 150, 200, 250]
    results = []

    for units in units_list:
        result = await simulate_swap(client, offer_address, ask_address, str(units), slippage_tolerance)
        received_units = result.ask_units
        results.append({'offered_units': units, 'received_units': float(received_units)})
        print(f"Offered Units: {units}, Received Units: {received_units}")

    await plot_swap_results(results, units_list)

if __name__ == '__main__':
    asyncio.run(main())
