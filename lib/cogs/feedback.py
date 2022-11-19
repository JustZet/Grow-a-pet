import discord
from discord.ext import commands

import sys
sys.path.append("lib")
from core.interface.feedback_modal import FeedbackModal


        
class Feedback(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot


        @self.bot.tree.command(name="feedback", description="Send bot feedback")
        async def feedback(interaction: discord.Interaction):

            await interaction.response.send_modal(FeedbackModal())
            
                
async def setup(bot):
    await bot.add_cog(Feedback(bot))