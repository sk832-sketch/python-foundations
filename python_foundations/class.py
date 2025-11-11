# Classes
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

# Creating instances (objects) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Accessing attributes
print(f"{dog1.name} is a {dog1.species} and is {dog1.age} years old.")
print(f"{dog2.name} is a {dog2.species} and is {dog2.age} years old.")

# Calling methods
print(dog1.bark())
print(dog2.bark())

#adding more