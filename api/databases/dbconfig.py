from dataclasses import dataclass


@dataclass
class Profiles:
     host: str = "localhost"
     port: int = 27017
     
     database: str = "growAPet"
     collection: str = "profiles"

@dataclass
class Pets:
     host: str = "localhost"
     port: int = 27017
     
     database: str = "growAPet"
     collection: str = "pets"




@dataclass
class Databases:
     profiles: Profiles = Profiles
     pets: Pets = Pets
