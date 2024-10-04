# 10. Получение статистики DEX за определенный период времени.



from stonfi import APIClient
import asyncio
async def main():
    client = APIClient()
    print(await client.get_dex_stats("2023-01-01T00:00:00", "2023-01-01T00:30:00"))
if __name__ == '__main__':
    asyncio.run(main())