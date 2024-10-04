# 3. Получение списка всех доступных ферм.


from stonfi import APIClient
import asyncio
async def main():
    client = APIClient()
    print(await client.get_farms())

if __name__ == '__main__':
    asyncio.run(main())