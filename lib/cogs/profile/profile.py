

import sys
import asyncio
from dataclasses import asdict
from datetime import datetime
import discord
from discord.ext import commands
import traceback

sys.path.append("lib")
from core.data.pet_profile.repositories.pet_profile_repository import PetProfileRepository, PetProfileModel
from core.config import *

from cogs.profile.create.create_profile import create_profile
from cogs.profile.reset.reset_profile import reset_profile
from cogs.profile.show_profile.show_profile import show_profile
from cogs.profile.delete.delete_profile import delete_profile

pet_profile_repo = PetProfileRepository()


class CreateProfile(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        
        @self.bot.tree.command(name="create", description="Create pet profile")
        async def create(interaction: discord.Interaction):
            await create_profile(interaction= interaction)
            
            
        @self.bot.tree.command(name="reset", description="Reset your pet profile")
        async def reset(interaction: discord.Interaction):
            await reset_profile(interaction= interaction)
            
        @self.bot.tree.command(name="delete", description="Permanently delete your pet profile")
        async def delete(interaction: discord.Interaction):
            await delete_profile(interaction= interaction)
            
            
        @self.bot.tree.command(name="profile", description="Shows your pet profile")
        async def profile(interaction: discord.Interaction):
            await show_profile(interaction= interaction)
            
            

    
        
        
                
                
async def setup(bot):
    await bot.add_cog(CreateProfile(bot))