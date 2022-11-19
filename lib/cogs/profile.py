import sys
import asyncio
from dataclasses import asdict
from datetime import datetime
import discord
from discord.ext import commands
import traceback


sys.path.append("lib")
from databases.mongodb import MongoDatabase
from core.interface.embeds import Embeds
from core.models.profile import ProfileModel
from core.config import *

db = MongoDatabase()


class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot


        @self.bot.tree.command(name="profile", description="Show your pet profile")
        async def profile(interaction: discord.Interaction):
            
            user_id = interaction.user.id
            
            db = MongoDatabase()
            user_exists = db.exists_in_db({"userId": user_id})
            
            if user_exists:

                embed = Embeds().basic_embed(
                title="Profile",
                description=f'Welcome back {interaction.user.display_name}',
                thubnail=Images.BOT_AVATAR,
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
                
            else:
                embed = Embeds().basic_embed(
                title="Profile",
                description=f'Welcome {interaction.user.display_name}, you don t have a profile, do you want to create one? \n Please use the following commands :)',
                thubnail=Images.BOT_AVATAR,
                )
                embed.add_field(inline=True, name='/create', value=f'{Emojis.KISS} Create pet profile ')
                await interaction.response.send_message(embed=embed, ephemeral=True)


            


        
            
                
                
async def setup(bot):
    await bot.add_cog(Profile(bot))