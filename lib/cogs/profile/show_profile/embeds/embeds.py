import sys

sys.path.append("lib")
from core.interface.embeds import Embeds
from core.config import *


# profile = Embeds().basic_embed(
# title="Profile",
# description=f'Welcome back {interaction.user.display_name}',
# thubnail=Images.BOT_AVATAR,
# )

profile_not_found_embed = Embeds().basic_embed(
    title="Profile",
    description=f'You don t have a pet profile, do you want to create one?',
    thubnail=Images.BOT_AVATAR,
)