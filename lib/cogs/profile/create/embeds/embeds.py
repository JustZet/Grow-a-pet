import sys

sys.path.append("lib")
from core.interface.embeds import Embeds
from core.config import *

create_profile_embed=Embeds().basic_embed(
    title="Create profile",
    description=f'Create your pet profile {Emojis.CLOUD} \n Use the view buttons to create your dream pet \n {Emojis.FOXGIRL} Are you ready?',
    thubnail="https://raw.githubusercontent.com/JustZet/Grow-a-pet/main/assets/bot/avatar.png",
)

profile_exists_embed = Embeds().basic_embed(
    title="Create profile",
    description='hmm, it seems that you already have a pet profile, if you want to delete it or restart, you can use the following command:',
    thubnail=Images.BOT_AVATAR,
)
profile_exists_embed.add_field(
    inline=True, 
    name='/reset', 
    value=f'{Emojis.RECYCLE_BIN} Reset your profile'
)

created_profile_embed = Embeds().basic_embed(
    title=f"{Emojis.CLOUD} Yay",
    description=f'{Emojis.FOXGIRL} Your profile successfully created', 
    thubnail=Images.BOT_AVATAR,
)      
