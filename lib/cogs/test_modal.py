import discord
from discord.ext import commands
from discord import app_commands

import sys
sys.path.append("lib")
from core.interface.feedback_modal import FeedbackModal

import sys
import asyncio

from datetime import datetime
import discord
from discord.ext import commands
import traceback


sys.path.append("lib")
from databases.mongodb import MongoDatabase



class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Green', style=discord.ButtonStyle.green, custom_id='persistent_view:green')
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is green.', ephemeral=True)

    @discord.ui.button(label='Red', style=discord.ButtonStyle.red, custom_id='persistent_view:red')
    async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is red.', ephemeral=True)

    @discord.ui.button(label='Grey', style=discord.ButtonStyle.grey, custom_id='persistent_view:grey')
    async def grey(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is grey.', ephemeral=True)


class FeedbackModal(discord.ui.Modal, title='Feedback'):
    
    name = discord.ui.TextInput(
        label='Name',
        placeholder='Your pet name here...',
        row=2,
        style=discord.TextStyle.paragraph,
        
        
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your feedback, {self.name.value}!', ephemeral=True, view=PersistentView())

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        traceback.print_tb(error.__traceback__)
        
class TestModal(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot


        @self.bot.tree.command(name="test_modal", description="Test modal sheet")

        async def test_modal(interaction: discord.Interaction):

            await interaction.response.send_modal(FeedbackModal())
            
                
async def setup(bot):
    await bot.add_cog(TestModal(bot))