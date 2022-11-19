import sys
from pymongo.results import InsertOneResult, DeleteResult, UpdateResult
from dataclasses import asdict

sys.path.append(".")
from databases.mongodb import MongoDatabase
from lib.core.data.pet_profile.models.pet_profile import PetProfileModel


class PetProfileLocalDatasource:
    
    def __init__(self):
        self.db = MongoDatabase()


    def get_pet_profile(self, userId: int) -> (PetProfileModel | None):
        query_pet: dict = {"userId": userId}
        pet_exists = self.db.exists_in_db(query_pet)
        
        if pet_exists:
            pet_profile_dict = self.db.find_table(query_pet)
            pet_profile = PetProfileModel(**pet_profile_dict)
            return pet_profile
        
        else: 
            return None
        
    
    def delete_pet_profile(self, userId: int) -> (DeleteResult | None):
        query_pet: dict = {"userId": userId}
        pet_exists = self.db.exists_in_db(query_pet)
        
        if pet_exists:
            delete_pet_profile = self.db.delete_tables(query_pet)
            return delete_pet_profile
        
        else: 
            return None
        
        
        
    
    def insert_pet_profile(self, profile: PetProfileModel)  -> (InsertOneResult | None):
        query_pet: dict = {"userId": profile.userId}
        pet_exists = self.db.exists_in_db(query_pet)
        
        
        if pet_exists:
            return None
        
        else: 
            dict_profile = asdict(profile)
            upload = self.db.upload_table(dict_profile)
            return upload
        
        
    def update_pet_profile(self, profile: PetProfileModel)  -> (UpdateResult | None):
        query_pet: dict = {"userId": profile.userId}
        pet_exists = self.db.exists_in_db(query_pet)
        
        
        if pet_exists:
            return None
        
        else: 
            query = {"userId": profile.userId}
            dict_profile = asdict(profile)
            upload = self.db.update_table(query, dict_profile)
            return upload