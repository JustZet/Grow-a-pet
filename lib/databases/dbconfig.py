from dataclasses import dataclass

# ? Databases configurations
@dataclass
class MongodbConfig:
     host: str = "localhost"
     port: int = 27017
     
     database: str = "discord"
     collection: str = "growAPet"
