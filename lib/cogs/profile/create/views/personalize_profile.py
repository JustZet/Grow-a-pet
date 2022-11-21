import sys
import asyncio
from dataclasses import asdict
from datetime import datetime
import discord
from discord.ext import commands
from pymongo.results import InsertOneResult, DeleteResult

import traceback


sys.path.append("lib")
from core.data.pet_profile.repositories.pet_profile_repository import PetProfileRepository, PetProfileModel
from core.config import *

from cogs.profile.create.embeds.embeds import profile_exists_embed, created_profile_embed



pet_profile_repo = PetProfileRepository()

class PersonalizeProfileView(discord.ui.View):
    
    def __init__(self):
        super().__init__()
        self.timeout = 100

    @discord.ui.button(label='Start', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        # profile = PetProfileModel(
        #     userId= interaction.user.id,
        #     userName= interaction.user.name,
        #     userDiscriminator= interaction.user.discriminator,
        #     userAccountCreatedAt= interaction.user.created_at,
        #     profileCreatedAt= datetime.now(),
        #     petId= 0,
        # )

        # pet_profile_repo.update_pet_profile(profile)
            
        pages = [profile_exists_embed, created_profile_embed, ]
    
        self.stop()

    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.delete_original_response()
        self.stop()
        