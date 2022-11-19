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
    _id: Optional[ObjectId] = None
    feedback: Optional[object] = None