import sys
import asyncio
from dataclasses import asdict
from datetime import datetime
import discord
from pymongo.results import InsertOneResult, DeleteResult

sys.path.append("lib")
from core.data.pet_profile.repositories.pet_profile_repository import PetProfileRepository
from core.config import *

from cogs.profile.reset.embeds.embeds import server_error_embed
from cogs.profile.delete.embeds.embeds import deleted_profile_embed, profile_not_found_embed

from cogs.profile.create.views.create_profile import CreateProfileView


class DeleteProfileView(discord.ui.View):
    
    def __init__(self):
        super().__init__()
        self.timeout = 100

    @discord.ui.button(emoji=Emojis.RECYCLE_BIN, style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        pet_profile_repo = PetProfileRepository()
        
        delete_profile = pet_profile_repo.delete_pet_profile(interaction.user.id)
        if isinstance(delete_profile, DeleteResult):
            await interaction.response.send_message(ephemeral=True, embed=deleted_profile_embed, view=CreateProfileView())
                
        elif delete_profile == None:
            await interaction.response.send_message(ephemeral=True, embed=profile_not_found_embed)
        
        else:
            await interaction.response.send_message(ephemeral=True, embed=server_error_embed)

    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.delete_original_response()
     
