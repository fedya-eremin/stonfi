# 7. Получение списка активов, принадлежащих определенному кошельку.

from stonfi import APIClient
import asyncio
async def main():
    client = APIClient()
    print(await client.get_wallet_assets("EQDYzZmfsrGzhObKJUw4gzdeIxEai3jAFbiGKGwxvxHinaPP"))

if __name__ == '__main__':
    asyncio.run(main())