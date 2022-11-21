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

from cogs.profile.delete.embeds.embeds import profile_not_found_embed, delete_profile_embed
from cogs.profile.delete.views.delete_profile import DeleteProfileView
from cogs.profile.create.views.create_profile import CreateProfileView
from cogs.profile.create.views.profile_exists import ProfileExitsView


pet_profile_repo = PetProfileRepository()

async def delete_profile(interaction: discord.Interaction):
    
    if pet_profile_repo.get_pet_profile(interaction.user.id) != None:
        await interaction.response.send_message(embed=delete_profile_embed, ephemeral=True, view=DeleteProfileView())
        
    else:
        await interaction.response.send_message(embed=profile_not_found_embed, view=CreateProfileView(), ephemeral=True)

