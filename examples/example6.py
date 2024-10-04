# 6. Симуляция операции обмена.


from stonfi import APIClient
import asyncio
from stonfi.types import SwapSimulateData
async def main():
    client = APIClient()
    print(await client.swap_simulate(SwapSimulateData(
        offer_address="EQBynBO23ywHy_CgarY9NK9FTz0yDsG82PtcbSTQgGoXwiuA",
        ask_address="EQCM3B12QK1e4yZSf8GtBRT0aLMNyEsBc_DhVfRRtOEffLez",
        units="100",
        slippage_tolerance="0.01"
    )))

if __name__ == '__main__':
    asyncio.run(main())