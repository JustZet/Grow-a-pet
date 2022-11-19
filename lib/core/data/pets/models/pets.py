from typing import List
from dataclasses import dataclass

from pet import PetModel

@dataclass
class PetsModel:
    allResultsNumber: int
    pets: List[PetModel]