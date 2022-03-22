# https://realpython.com/python3-object-oriented-programming/

class Dog:
    species = "Canis familiaris" # A class attribute that is static for all Dog objects
    def __init__(self, name, age): # The properties that all Dog objects must have are defined in a method called .__init__()
                                    # Every time a new Dog object is created, .__init__() sets the initial state of the object 
                                    # by assigning the values of the object’s properties. That is, .__init__() initializes each 
                                    # new instance of the class.
        self.name = name # sets name attribute
        self.age = age # sets age attribute


# example in practice:
dog1 = Dog("Shiloh", 1) # creates new instance of Dog
dog1.name # calls name attribute
dog1.age # calls age attribute
dog1.species # calls a class attribute


buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

buddy == miles # false

# attributes can still be changed dynamically
miles.species = 'Felis silvestris'
miles.species
miles.age = 999
miles.age

#########################################################
############################ INSTANCE METHODS ###########

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name # assigning name it itself
        self.age = age # assigning age to itself

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound): # assigns sound to itself
        return f"{self.name} says {sound}"
    

dog2 = Dog("Shiloh", 1)
dog2.age
dog2.name
dog2.description()
dog2.speak("Woof!")

# When writing your own classes, it’s a good idea to have a method that returns 
# a string containing useful information about an instance of the class.



class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name # assigning name it itself
        self.age = age # assigning age to itself

    # Instance method
    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound): # assigns sound to itself
        return f"{self.name} says {sound}"
    

dog3 = Dog("Shiloh", 1)
dog3.__str__() # instead of .description(). There doesn't seem to be anything *inherently*
                # wrong with using .description(), except that it isn't the most 'pythonic'
                # way of doing things.

# Methods like .__init__() and .__str__() are called dunder methods because 
# they begin and end with double underscores. 

#################################
# Exercise:

# Create a Car class with two instance attributes:

# .color, which stores the name of the car’s color as a string
# .mileage, which stores the number of miles on the car as an integer
# Then instantiate two Car objects—a blue car with 20,000 miles and 
# a red car with 30,000 miles—and print out their colors and mileage. Your output should look like this:

# The blue car has 20,000 miles.
# The red car has 30,000 miles.


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


car1 = Car("blue", 20000)
car2 = Car("red", 30000)
car1.__str__()
car2.__str__()











