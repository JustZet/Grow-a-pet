
import discord


class Embeds:
    def __init__(self): 
        self.icon_url = "https://raw.githubusercontent.com/JustZet/Grow-a-pet/main/assets/bot/avatar.png"
        self.footer_text = "Grow me a pet"
    
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
       
        
    
       
    def error_embed(
    self,
    title: str = None, 
    description: str = None,
    ) -> discord.Embed:
        
        embed = discord.Embed(
            title=title,
            description=description,
            color=discord.colour.Color.random,
            )
        return embed
        
    
