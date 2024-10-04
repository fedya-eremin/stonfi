# 8. Получение подробной информации о конкретном активе, принадлежащем определенному кошельку.


from stonfi import APIClient
import asyncio
async def main():
    client = APIClient()
    print(await client.get_wallet_asset("EQDYzZmfsrGzhObKJUw4gzdeIxEai3jAFbiGKGwxvxHinaPP","EQDwlPXvgDemNYEjEaJw8vxh9bYPqC--w2NnqFryU6Ae6Eoz"))

if __name__ == '__main__':
    asyncio.run(main())