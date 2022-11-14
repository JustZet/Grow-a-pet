# from dbconfig import Databases as db
import sys
from dataclasses import dataclass

import pymongo
from pymongo.errors import DuplicateKeyError

sys.path.append("lib/databases")
# from dbconfig import MongoDb as db

from dbconfig import MongodbConfig as db


@dataclass
class MongoDatabase: # Connect to MongoDB:
    """This is connection with local mongo database."""
    host = db.host
    port = db.port
    mdb = db.database
    col = db.collection
    
    conn = pymongo.MongoClient(host, port)
    database = conn[mdb]
    collection = database[col]

    def dbCollection(self):
        """Return collection."""
        return self.collection

    def count_elements(self, query) -> int:
        
        return self.collection.count_documents(query)


    def find(self):
        return self.collection.find()
    
    def find_last_table(self):
        last_table = self.collection.find_one({"$query": {}, "$orderby": {"$natural" : -1}})
        return last_table
    
    def find_table(self, query):
        """
        Find single table using query , 
        for example `find_table({id: 12345})`
        """
        
        return self.collection.find_one(query)

    def find_tables(self, query = None):
        """
        Find multiple tables, 
        for example `find_tables({archive: 1})`
        """
        
        return self.collection.find(query)
        
    def update_table(self, filter, update):
        """
        Update single table in mongodatabase, 
        example `update_table({id: 123}, {id: 12})`
        """
        return self.collection.update_one(filter=filter, update={"$set": update})
    
    def upload_table(self, data):
        """
        Upload single table, example 
        `upload_table({id: 123})`
        """

        return self.collection.insert_one(data)

    
    def upload_tables(self, data):
        """
        Upload multiple tables, 
        example `upload_table({archive: 1})`
        """
        return self.collection.insert_many(data)
    
    def delete_table(self, query):
        """
        Delete one single table, 
        example `delete_table({id: 123})`
        """
        return self.collection.delete_one(query)

    def delete_tables(self, query):
        """
        Delete one single table, 
        example `delete_tables({id: 123})`
        """
        return self.collection.delete_many(query)
    
    def exists_in_db(self, query: dict[str, any]) -> bool:
        count = self.count_elements(query)
        if count == 0:
            return False
        else:
            return True
    
            

if __name__ == "__main__":
    from multiprocessing.pool import Pool as pool
    from time import time
    start = time()
    
    mongodb = MongoDatabase()

    m = mongodb.collection
    f = m.find()
    print(len(f))
    # syncron -> 500 tabele in 0.68 secunde...
    
