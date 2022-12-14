import sys
import asyncio

from datetime import datetime
import discord
from discord.ext import commands
import traceback


sys.path.append("lib")
from databases.mongodb import MongoDatabase

class FeedbackModal(discord.ui.Modal, title='Feedback'):
    
    name = discord.ui.TextInput(
        label='Name',
        placeholder='Your name here...',
    )
    feedback = discord.ui.TextInput(
        label='What do you think of this new feature?',
        style=discord.TextStyle.long,
        placeholder='Type your feedback here...',
        required=False,
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
        db = MongoDatabase()
        feedback = {
            "name": self.name.value,
            "feed": self.feedback.value,
            "date": datetime.now(),
        }
        
        
        db.update_table({"userId": interaction.user.id}, {"feedback": feedback})
        
        await interaction.response.send_message(f'Thanks for your feedback, {self.name.value}!', ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        traceback.print_tb(error.__traceback__)