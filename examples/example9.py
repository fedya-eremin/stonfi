# 9. Получение списка ферм, связанных с определенным кошельком.


from stonfi import APIClient
import asyncio
async def main():
    client = APIClient()
    print(await client.get_wallet_farms("EQDYzZmfsrGzhObKJUw4gzdeIxEai3jAFbiGKGwxvxHinaPP"))

if __name__ == '__main__':
    asyncio.run(main())