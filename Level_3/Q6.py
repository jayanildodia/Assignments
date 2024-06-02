# Create the custom Python classes which have methods and
# attributes and implement single inheritance, multiple inheritance,
# and multilevel inheritance

class Animal:  # Base class for single and multilevel inheritance
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

class Dog(Animal):  # Single inheritance: Dog class inherits from Animal
    def speak(self):
        return "Bark"

class Walker:  # Another base class for multiple inheritance
    def walk(self):
        return "Walking"

class Duck(Animal, Walker): # Multiple inheritance: Duck class inherits from Animal and Walker
    def quack(self):
        return "Quack"

class Puppy(Dog):  # Multilevel inheritance: Puppy class inherits from Dog
    def play(self):
        return "Playing"

dog = Dog("Buddy")  # Single inheritance example
print(f"Dog: {dog.name}, Sound: {dog.speak()}")

duck = Duck("Daffy")  # Multiple inheritance example
print(f"Duck: {duck.name}, Sound: {duck.speak()}, Walk: {duck.walk()}, Quack: {duck.quack()}")

puppy = Puppy("Max")  # Multilevel inheritance example
print(f"Puppy: {puppy.name}, Sound: {puppy.speak()}, Play: {puppy.play()}")
