from dataclasses import dataclass

from datetime import datetime
from bson.objectid import ObjectId
from typing import Optional
from pet_profile import PetProfileModel


@dataclass
class UserProfileModel:
    userId: int
    userName: str
    userDiscriminator: str
    userAccountCreatedAt: datetime
    petProfile: PetProfileModel
    feedback: Optional[object] = None