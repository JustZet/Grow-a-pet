import sys
import asyncio
from dataclasses import asdict
from datetime import datetime
import discord
from discord.ext import commands
import traceback


sys.path.append("lib")
from core.interface.embeds import Embeds
from core.data.pet_profile.repositories.pet_profile_repository import PetProfileRepository, PetProfileModel
from core.models.profile import ProfileModel
from core.config import *

profile_exists_embed = Embeds().basic_embed(
    title="Create profile",
    description=f'hmm, it seems that you already have a pet profile, if you want to delete it or restart, you can use the following command:',
    thubnail=Images.BOT_AVATAR,
)
profile_exists_embed.add_field(
    inline=True, 
    name='/reset', 
    value=f'{Emojis.RECYCLE_BIN} Reset your profile'
)

created_profile_embed = Embeds().basic_embed(
    title=f"{Emojis.CLOUD} Yay",
    description=f'{Emojis.FOXGIRL} Your profile successfully created', 
    thubnail=Images.BOT_AVATAR,
)      

pet_profile_repo = PetProfileRepository()

class PersonalizeProfile(discord.ui.View):
    
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
        
     


class CreateProfileButtons(discord.ui.View):
    
    def __init__(self):
        super().__init__()
        self.timeout = 100

    @discord.ui.button(label='Start', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        profile = PetProfileModel(
            userId= interaction.user.id,
            userName= interaction.user.name,
            userDiscriminator= interaction.user.discriminator,
            userAccountCreatedAt= interaction.user.created_at,
            profileCreatedAt= datetime.now(),
            petId= 0,
        )
    

        pet_profile_repo.insert_pet_profile(profile)
        
        
    
        await interaction.response.send_message(ephemeral=True, embed=created_profile_embed, view=PersonalizeProfile())
        
        
 

    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.delete_original_response()
        
     
buttons = CreateProfileButtons()
        
class CreateProfile(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot


        @self.bot.tree.command(name="create", description="Create pet profile")
        async def create(interaction: discord.Interaction):
            
            if pet_profile_repo.get_pet_profile(interaction.user.id) != None:
                await interaction.response.send_message(embed=profile_exists_embed, ephemeral=True)
                
            else:
                embed=Embeds().basic_embed(
                title="Create profile",
                description=f'Create your pet profile {Emojis.CLOUD} \n Use the view buttons to create your dream pet \n {Emojis.FOXGIRL} Are you ready?',
                thubnail="https://raw.githubusercontent.com/JustZet/Grow-a-pet/main/assets/bot/avatar.png",
                )
                await interaction.response.send_message(embed=embed, view=buttons, ephemeral=True)
        

        
        
                
                
async def setup(bot):
    await bot.add_cog(CreateProfile(bot))