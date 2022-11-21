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
from core.config import *


reset_profile_embed=Embeds().basic_embed(
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
