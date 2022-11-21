import sys

sys.path.append("lib")
from core.interface.embeds import Embeds
from core.config import *

profile_not_found_embed = Embeds().basic_embed(
    title="Delete profile",
    description='hmm, it seems that you don\'t have an pet profile.. \n Do you want to create one?',
    thubnail=Images.BOT_AVATAR,
)

delete_profile_embed=Embeds().basic_embed(
    title="Delete profile",
    description=f'{Emojis.RECYCLE_BIN} Are you sure you want to delete your pet profile? \n All progress will be lost',
    thubnail="https://raw.githubusercontent.com/JustZet/Grow-a-pet/main/assets/bot/avatar.png",
)

deleted_profile_embed = Embeds().basic_embed(
    title=f"{Emojis.CLOUD}",
    description=f'{Emojis.CLOUD} Your profile successfully deleted, do you want to create another one?', 
    thubnail=Images.BOT_AVATAR,
)      
