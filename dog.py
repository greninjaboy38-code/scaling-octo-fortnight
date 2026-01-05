class Dog:
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def display(self):
        print("Name:", self.name, "Breed:", self.breed, "Species:", Dog.species)

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "German Shepherd")

dog1.display()
dog2.display()
