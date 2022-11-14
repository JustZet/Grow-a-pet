import sys

import discord
from discord.ext import commands

sys.path.append("lib")
from databases.mongodb import MongoDatabase
from core.interface.embeds import Embeds

db = MongoDatabase()

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Create', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        table = {
            "userId": interaction.user.id,
            "userName": interaction.user.name,

        }
        db.upload_table(table)
        await interaction.response.send_message('Profile successfully created', ephemeral=True)
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        self.value = False
        self.stop()
        
        
        
class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot


        @self.bot.tree.command(name="profile", description="Show your pet profile")
        async def profile(interaction: discord.Interaction):
            
            
            user_id = interaction.user.id
            user_exists = db.exists_in_db({"userId": user_id})
            
            if user_exists:
                
                embd=Embeds().basic_embed(
                    
                title=interaction.user.display_name,
                description='Welcome back user',
                )
        
                await interaction.response.send_message(embed=embd)

            else:
                embd=Embeds().basic_embed(
                title="Account",
                description=f'Welcome {interaction.user.display_name}, you don t have a profile, do you want to create one? :)',
          
                )
                await interaction.response.send_message(embed=embd)
            
        # @self.bot.tree.command(name="delete", description="Delete your pet profile")
        # async def delete(interaction: discord.Interaction):
        #     user_id: str = interaction.user.id
            
            
            


        
            
                
                
async def setup(bot):
    await bot.add_cog(Profile(bot))