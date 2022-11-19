import sys
import asyncio
from dataclasses import asdict
from datetime import datetime
import discord
from discord.ext import commands
import traceback
from pymongo.results import InsertOneResult, DeleteResult

sys.path.append("lib")
from core.interface.embeds import Embeds
from core.data.pet_profile.repositories.pet_profile_repository import PetProfileRepository, PetProfileModel
from core.models.profile import ProfileModel
from core.config import *

sys.path.append(".")
from databases.mongodb import MongoDatabase

reset_main_message=Embeds().basic_embed(
    title="Reset profile",
    description=f'Do you want to reset your pet profile? {Emojis.RECYCLE_BIN} \n All progress will be lost \n {Emojis.CLOUD} Are you sure?',
    thubnail=Images.BOT_AVATAR,
)

profile_exists_embed = Embeds().basic_embed(
    title="Create profile",
    description=f'hmm, it seems that you already have a pet profile, if you want to delete it or restart, you can use the following command:',
    thubnail=Images.BOT_AVATAR,
)
profile_exists_embed.add_field(
    inline=True, 
    name='/reset', 
    value=f'{Emojis.COOKIES} Reset your profile'
)
profile_exists_embed.add_field(
    inline=True,
    name='/delete', 
    value=f'{Emojis.RECYCLE_BIN} Forever delete your profile',
)
profile_exists_embed.add_field(
    inline=False,
    name='/disconnect', 
    value=f'{Emojis.RECYCLE_BIN} Disconnect from your current pet profile',
)

server_error_embed = Embeds().basic_embed(
    title=f"{Emojis.CLOUD} Bruh -.-",
    description=f'{Emojis.FOXGIRL} Server error occured, please try again later -.-', 
    thubnail=Images.BOT_AVATAR,
)      

not_found_profile_embed = Embeds().basic_embed(
    title=f"{Emojis.CLOUD} Hmm..",
    description=f'{Emojis.FOXGIRL} You don\'t have a pet profile, do you want to create one?', 
    thubnail=Images.BOT_AVATAR,
)      

reseted_profile_embed = Embeds().basic_embed(
    title=f"{Emojis.COOKIES} Yay",
    description=f'{Emojis.FOXGIRL} Your profile was succesful reseted', 
    thubnail=Images.BOT_AVATAR,
)      

class ResetProfileButtons(discord.ui.View):
    
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
     
buttons = ResetProfileButtons()
        
class ResetProfile(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot


        @self.bot.tree.command(name="reset", description="Reset your pet profile")
        async def reset(interaction: discord.Interaction):
        

            await interaction.response.send_message(embed=reset_main_message, view=buttons, ephemeral=True)
    

    
        
                
                
async def setup(bot):
    await bot.add_cog(ResetProfile(bot))