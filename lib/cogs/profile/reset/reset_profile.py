import sys
import asyncio
from dataclasses import asdict
from datetime import datetime
import discord
from discord.ext import commands
import traceback
from pymongo.results import InsertOneResult, DeleteResult

sys.path.append("lib")
from core.config import *

from cogs.profile.reset.embeds.embeds import *
from cogs.profile.reset.views.reset_profile import ResetProfileView



async def reset_profile(interaction: discord.Interaction):
    await interaction.response.send_message(embed=reset_profile_embed, view=ResetProfileView(), ephemeral=True)

