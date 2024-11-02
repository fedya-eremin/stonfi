from stonfi import APIClient
import asyncio
from collections import defaultdict
import matplotlib.pyplot as plt

async def main():
    client = APIClient()
    assets = await client.get_assets()

    tag_count = defaultdict(int)

    for ads in assets:
        for tag in ads.tags:
            tag_count[tag] += 1

    tag_count = dict(tag_count)

    plt.figure(figsize=(10, 6))
    plt.bar(tag_count.keys(), tag_count.values(), color='skyblue')
    plt.xlabel('Tags')
    plt.ylabel('Count')
    plt.title('Tag Counts')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    asyncio.run(main())
