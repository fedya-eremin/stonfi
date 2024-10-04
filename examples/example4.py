# 4. Получение подробной информации о конкретной ферме.


from stonfi import APIClient
import asyncio
async def main():
    client = APIClient()
    print(await client.get_farm("EQDEy0W_ghj7Hho2zIm0sTMTppDowUzCQCp59AY_YgAQWIPC"))

if __name__ == '__main__':
    asyncio.run(main())