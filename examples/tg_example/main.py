import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command, CommandObject
from stonfi import APIClient

logging.basicConfig(level=logging.INFO)

TOKEN = "API_TOKEN"
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

api_client = APIClient()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        "Hello! I am the Ston.fi bot. Use the commands:\n"
        "/assets - get 10 random assets\n"
        "/farms - get 10 random farms\n"
        "/markets - get 10 trading pairs\n"
        "/get_wallet_assets <wallet> - get 10 assets of the wallet\n"
        "/get_wallet_farms <wallet> - get 10 farms of the wallet\n"
        "/get_wallet_pools <wallet> - get 10 pools of the wallet\n"
    )

@dp.message(Command("assets"))
async def get_assets(message: types.Message):
    assets = await api_client.get_assets()
    if assets:
        asset_names = [f"{asset.symbol} {asset.dex_price_usd or '???'} USD" for asset in assets[:10]]
        await message.answer("10 random assets:\n" + "\n".join(asset_names))
    else:
        await message.answer("Failed to retrieve assets.")

@dp.message(Command("farms"))
async def get_farms(message: types.Message):
    farms = await api_client.get_farms()
    if farms:
        farm_names = [f"{farm.minter_address}, {farm.locked_total_lp_usd} USD" for farm in farms[:10]]
        await message.answer("10 random farms:\n" + "\n".join(farm_names))
    else:
        await message.answer("Failed to retrieve farms.")

@dp.message(Command("markets"))
async def get_markets(message: types.Message):
    markets = await api_client.get_markets()
    if markets:
        market_pairs = [" vs ".join(pair) for pair in markets[:10]]
        await message.answer("\n".join(market_pairs))
    else:
        await message.answer("Failed to retrieve trading pairs.")

@dp.message(Command("get_wallet_assets"))
async def get_wallet_assets(message: types.Message, command: CommandObject):
    wallet_addr = command.args
    if wallet_addr:
        assets = await api_client.get_wallet_assets(wallet_addr)
        if assets:
            asset_names = [f"{asset.symbol} - Balance {asset.balance or '???'}" for asset in assets[:10]]
            await message.answer("10 random assets of the wallet:\n" + "\n".join(asset_names))
        else:
            await message.answer("Failed to retrieve wallet assets.")
    else:
        await message.answer("Please specify a wallet address.")

@dp.message(Command("get_wallet_farms"))
async def get_wallet_farms(message: types.Message, command: CommandObject):
    wallet_addr = command.args
    if wallet_addr:
        farms = await api_client.get_wallet_farms(wallet_addr)
        if farms:
            farm_names = [farm.nft_infos for farm in farms[:10]]
            await message.answer("10 random farms of the wallet:\n" + "\n".join(farm_names))
        else:
            await message.answer("Failed to retrieve farms for this wallet.")
    else:
        await message.answer("Please specify a wallet address.")

@dp.message(Command("get_wallet_pools"))
async def get_wallet_pools(message: types.Message, command: CommandObject):
    wallet_addr = command.args
    if wallet_addr:
        pools = await api_client.get_wallet_pools(wallet_addr)
        if pools:
            pool_names = [pool.address for pool in pools[:10]]
            await message.answer("10 random pools of the wallet:\n" + "\n".join(pool_names))
        else:
            await message.answer("Failed to retrieve pools for this wallet.")
    else:
        await message.answer("Please specify a wallet address.")

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())