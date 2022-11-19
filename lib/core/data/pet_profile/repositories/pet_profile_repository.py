import sys
from pymongo.results import InsertOneResult, DeleteResult

sys.path.append(".")
from lib.core.data.pet_profile.datasources.local_profiles import PetProfileLocalDatasource
from lib.core.data.pet_profile.models.pet_profile import PetProfileModel

local_data_source = PetProfileLocalDatasource()

class PetProfileRepository:
    
        
    def insert_pet_profile(self, profile: PetProfileModel) -> InsertOneResult | None:
        pet_profile  = local_data_source.insert_pet_profile(profile)
        return pet_profile
    
    def update_pet_profile(self, profile: PetProfileModel) -> InsertOneResult | None:
        pet_profile  = local_data_source.insert_pet_profile(profile)
        return pet_profile



    def get_pet_profile(self, userId: int) -> PetProfileModel | None:
        pet_profile  = local_data_source.get_pet_profile(userId)
        return pet_profile

    def delete_pet_profile(self, userId: int) -> DeleteResult | None:
        pet_profile  = local_data_source.delete_pet_profile(userId)
        return pet_profile