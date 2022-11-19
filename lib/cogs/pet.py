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


class PetProfile(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot


        @self.bot.tree.command(name="pet", description="Show a pet")
        async def pet(interaction: discord.Interaction):
            
            embed = Embeds().basic_embed(
            title="Great Dane",
            description=f'Bark bark...',
            thubnail="https://raw.githubusercontent.com/JustZet/Grow-a-pet/main/assets/dogs/1.png",
            )
            embed.set_image(url="https://i.pinimg.com/originals/4a/69/36/4a69361828d44c8742815ce1ca694c65.png")
            
            await interaction.response.send_message(embed=embed, ephemeral=True)


        
            
                
                
async def setup(bot):
    await bot.add_cog(PetProfile(bot))