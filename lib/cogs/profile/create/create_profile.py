import sys
import asyncio
from dataclasses import asdict
from datetime import datetime
import discord
from discord.ext import commands
import traceback

sys.path.append("lib")
from core.data.pet_profile.repositories.pet_profile_repository import PetProfileRepository
from core.config import *

from cogs.profile.create.embeds.embeds import profile_exists_embed, create_profile_embed
from cogs.profile.create.views.create_profile import CreateProfileView
from cogs.profile.create.views.profile_exists import ProfileExitsView


pet_profile_repo = PetProfileRepository()

async def create_profile(interaction: discord.Interaction):
    
    if pet_profile_repo.get_pet_profile(interaction.user.id) != None:
        await interaction.response.send_message(embed=profile_exists_embed, view=ProfileExitsView(), ephemeral=True)
        
    else:
        await interaction.response.send_message(embed=create_profile_embed, view=CreateProfileView(), ephemeral=True)

