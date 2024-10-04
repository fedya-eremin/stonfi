# 1. Получение списка всех доступных активов.
from stonfi import APIClient
import asyncio
async def main():
    client = APIClient()
    print(await client.get_assets())

if __name__ == '__main__':
    asyncio.run(main())

    