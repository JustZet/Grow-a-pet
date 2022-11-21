
import discord
import sys
sys.path.append("lib")
from core.config import *

class Embeds:
    def __init__(self): 
        self.icon_url = Images.BOT_AVATAR
        self.footer_text = "Grow a pet"
    
    def basic_embed(
    self,
    title: str = None, 
    description: str = None,
    thubnail: str = None,
    image: str = None,
    
    ) -> discord.Embed:
        
        embed =  discord.Embed(
            title=title,
            description=description,
            color=0x002934,
            )
        
        embed.set_image(url=image)
        embed.set_thumbnail(url=thubnail)
        embed.set_footer(icon_url=self.icon_url, text=self.footer_text)
        return embed
       
        
    def profile_not_found(self):
        
        return self.basic_embed(
            title="Delete profile",
            description='hmm, it seems that you don\'t have an pet profile.. \n Do you want to create one?',
            thubnail=Images.BOT_AVATAR,
        )
