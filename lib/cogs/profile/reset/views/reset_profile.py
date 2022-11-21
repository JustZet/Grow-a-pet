import sys
import asyncio
from dataclasses import asdict
from datetime import datetime
import discord
from pymongo.results import InsertOneResult, DeleteResult

sys.path.append("lib")
from core.data.pet_profile.repositories.pet_profile_repository import PetProfileRepository, PetProfileModel
from core.config import *

from cogs.profile.reset.embeds.embeds import *



class ResetProfileView(discord.ui.View):
    
    def __init__(self):
        super().__init__()
        self.timeout = 100

    @discord.ui.button(label='Yes, reset it', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        pet_profile_repo = PetProfileRepository()
        
        delete_profile = pet_profile_repo.delete_pet_profile(interaction.user.id)
        if isinstance(delete_profile, DeleteResult):
            
            pet_profile = PetProfileModel(
                    userId= interaction.user.id,
                    userName= interaction.user.name,
                    userDiscriminator= interaction.user.discriminator,
                    userAccountCreatedAt= interaction.user.created_at,
                    profileCreatedAt= datetime.now(),
                    petId= 0,
            )
            insert_profile = pet_profile_repo.insert_pet_profile(pet_profile)
            
            
            if isinstance(insert_profile, InsertOneResult):
                await interaction.response.send_message(ephemeral=True, embed=reseted_profile_embed)
                
            elif insert_profile == None:
                await interaction.response.send_message(ephemeral=True, embed=server_error_embed)
        
            else:
                await interaction.response.send_message(ephemeral=True, embed=server_error_embed)
            
                
        elif delete_profile == None:
            await interaction.response.send_message(ephemeral=True, embed=not_found_profile_embed)
        
        else:
            await interaction.response.send_message(ephemeral=True, embed=server_error_embed)
            


    @discord.ui.button(label='No', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.delete_original_response()
     
