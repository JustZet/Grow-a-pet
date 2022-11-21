import sys
import asyncio
from dataclasses import asdict
from datetime import datetime
import discord
from discord.ext import commands

sys.path.append("lib")
from core.config import *

from cogs.profile.create.embeds.embeds import profile_exists_embed, created_profile_embed
from cogs.profile.delete.embeds.embeds import delete_profile_embed
from cogs.profile.reset.embeds.embeds import reset_profile_embed

from cogs.profile.delete.views.delete_profile import DeleteProfileView
from cogs.profile.reset.views.reset_profile import ResetProfileView

class ProfileExitsView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.timeout = 100
    
    @discord.ui.button(label='Reset', style=discord.ButtonStyle.blurple)
    async def reset(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed=reset_profile_embed, ephemeral=True, view= ResetProfileView())
                
    @discord.ui.button(label='Delete', style=discord.ButtonStyle.red)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed=delete_profile_embed, ephemeral=True, view= DeleteProfileView())
        
        
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.delete_original_response()
        self.stop()
        