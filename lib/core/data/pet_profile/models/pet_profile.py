from dataclasses import dataclass

from datetime import datetime
from bson.objectid import ObjectId
from typing import Optional


@dataclass
class PetProfileModel:
    userId: int
    userName: str
    userDiscriminator: str
    userAccountCreatedAt: datetime
    profileCreatedAt: datetime
    petId: int
    feedback: Optional[object] = None


# @dataclass
# class PetProfileModel:
#     id: int
#     name: str
#     # lastFed: datetime
#     # lastDrinkedWhater: datetime
#     level: int
#     profileCreatedAt: datetime
    
    