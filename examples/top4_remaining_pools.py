from stonfi import APIClient
import asyncio
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

async def main():
    client = APIClient()
    farms = await client.get_farms()

    data = []
    for farm in farms:
        farm_dict = vars(farm)
        for reward in farm_dict.get('rewards', []):
            if int(reward.remaining_rewards) > 1000:
                data.append({
                    'farm_name': farm_dict.get('pool_address', 'Unknown')[:4],
                    'remaining_rewards': int(reward.remaining_rewards)
                })

    df = pd.DataFrame(data)

    df_sorted = df.sort_values(by='remaining_rewards', ascending=False)

    top_4_df = df_sorted.head(4)

    print(top_4_df)
    sns.set(style="whitegrid")
    plt.figure(figsize=(14, 8))

    sns.barplot(x='farm_name', y='remaining_rewards', data=top_4_df)
    plt.title('Top 4 Farms by Remaining Rewards')
    plt.xlabel('Farm Name')
    plt.ylabel('Remaining Rewards')
    plt.yscale('log')  
    plt.show()

if __name__ == '__main__':
    asyncio.run(main())
