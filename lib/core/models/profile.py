from dataclasses import dataclass
from datetime import datetime

@dataclass
class ProfileModel:
    userId: int
    userName: str
    userDiscriminator: str
    userAccountCreatedAt: datetime
    profileCreatedAt: datetime
    petId: int