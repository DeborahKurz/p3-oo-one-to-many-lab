class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = "Steve"):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.add_pet_to_all(self)

    @property
    def pet_type(self):
        return self._pet_type 
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type    
        else:
            raise Exception("Pet type must be an the approved list")
        
    @classmethod
    def add_pet_to_all(cls, pet_type):
        cls.all.append(pet_type)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Pet type must be an the approved list")

    def get_sorted_pets(self):
        return sorted(self.pets(),key=lambda pet: pet.name)