import asyncio
import os

import discord
from discord.ext import commands
from core.config.config import Config

intents = discord.Intents.default()

# intents.message_content = True
bot = commands.Bot(command_prefix=Config.BOT_PREFIX, intents=intents)


# Set bot logged in message
@bot.event
async def on_ready():
	guild = discord.Object(id=Config.GUILD_ID)
 
	bot.tree.copy_global_to(guild=guild)
	await bot.tree.sync(guild=guild)
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')


# Load bot commands
async def load_cogs():
    for f in os.listdir(Config.COGS_DIR):
    	if f.endswith(".py"):
    		if f != "__init__.py":
    			await bot.load_extension("cogs." + f[:-3])
   
async def main():
	await load_cogs()


	await bot.start(Config.BOT_TOKEN)

if __name__ == "__main__":
	asyncio.run(main())


