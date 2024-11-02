from stonfi import APIClient
import asyncio
import pandas as pd
from datetime import datetime, timedelta

import time

async def get_dex_stats(start_time, end_time):
    client = APIClient()
    return await client.get_dex_stats(start_time, end_time)

async def main():
    for i in range(4):
        end_time = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        start_time = end_time - timedelta(days=30)

        dex_stats = await get_dex_stats(start_time.isoformat(), end_time.isoformat())

        print(dex_stats)
        now = start_time

        time.sleep(4)

if __name__ == '__main__':
    asyncio.run(main())
