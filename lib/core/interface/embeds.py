
import discord

class Embeds:
    
    def basic_embed(
    self,
    title: str = None, 
    description: str = None,
    thubnail: str = None,
    ) -> discord.Embed:
        
        return discord.Embed(
            title=title,
            description=description,
            color=0x002934,
            ).set_thumbnail(url=thubnail)
        
       
        
    
       
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
        
    
