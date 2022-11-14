import asyncio
import os

import discord
from discord.ext import commands
from const import *


intents = discord.Intents.default()

# intents.message_content = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)


@bot.event
async def on_ready():
	guild = discord.Object(id=GUILD_ID)
	# async with bot:

	bot.tree.copy_global_to(guild=guild)
	await bot.tree.sync(guild=guild)
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')


async def load_cogs():
    for f in os.listdir(COGS_DIR):
    	if f.endswith(".py"):
    		if f != "__init__.py":
    			await bot.load_extension("cogs." + f[:-3])
   
async def main():
	await load_cogs()


	await bot.start(BOT_TOKEN)

if __name__ == "__main__":
	asyncio.run(main())


