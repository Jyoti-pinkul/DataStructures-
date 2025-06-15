"""
Duck Typing	“If it quacks like a duck…” – based on behavior not inheritance
Operator Overloading	                  Same operator behaves differently for different types
Method Overriding	                      Subclass redefines parent class method
Function Overloading	                  Python does not support directly, but can mimic with *args
"""

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())  # Woof!
animal_sound(Cat())  # Meow!
