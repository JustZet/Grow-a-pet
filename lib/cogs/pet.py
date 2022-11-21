import sys
import asyncio
from dataclasses import asdict
from datetime import datetime
import discord
from discord.ext import commands
import traceback

sys.path.append(".")
from databases.mongodb import MongoDatabase

sys.path.append("lib")
from core.interface.embeds import Embeds
from core.config import *

db = MongoDatabase()


class PetProfile(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot


        @self.bot.tree.command(name="pet", description="Show a pet")
        async def pet(interaction: discord.Interaction):
            
            embed = Embeds().basic_embed(
            title="Great Dane",
            description=f'"Is a good dog, he don\'t bite, trust me 🤕..."',
            thubnail="https://raw.githubusercontent.com/JustZet/Grow-a-pet/main/assets/dogs/1.png",
            )
            embed.add_field(name="weight", value="100kg")
            embed.add_field(name="height", value="twice as much as you")
            embed.add_field(name="friendly", value="yes🤕..", inline=False)
            embed.add_field(name="name", value="what name he want", inline=False)

            await interaction.response.send_message(embed=embed, ephemeral=True)


        
            
                
                
async def setup(bot):
    await bot.add_cog(PetProfile(bot))