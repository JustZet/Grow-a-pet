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
from core.data.pet_profile.repositories.pet_profile_repository import PetProfileRepository

from cogs.profile.show_profile.embeds.embeds import profile_not_found_embed
from cogs.profile.create.views.create_profile import CreateProfileView


pet_profile_repo = PetProfileRepository()

async def show_profile(interaction: discord.Interaction):
        
    if pet_profile_repo.get_pet_profile(interaction.user.id) != None:
        await interaction.response.send_message("Not implemented yet..", ephemeral=True)
        
    else:
        await interaction.response.send_message(embed=profile_not_found_embed, view=CreateProfileView(), ephemeral=True)


    

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