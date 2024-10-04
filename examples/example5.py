# 5. Получение информации о конкретном пуле.



from stonfi import APIClient
import asyncio
async def main():
    client = APIClient()
    print(await client.get_pool("EQDMN87j_dg9BGVbtEfBHxjyQE3jNgnJnRgPtnWgXE1iOr_E"))

if __name__ == '__main__':
    asyncio.run(main())