class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create two objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
print(person2.greet())
# Hello, my name is Bob and I am 25 years old.
# ************************************************************************************************************************
# Inheritance
# Parent class (Vehicle)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"This is a {self.brand} {self.model}.")

# Child class (Car)
class Car(Vehicle):
    def __init__(self, brand, model, car_type):
        # Call the __init__ method of the parent class using super()
        super().__init__(brand, model)
        self.car_type = car_type  # Additional attribute for Car class

    def display_info(self):
        print(f"This is a {self.car_type} car: {self.brand} {self.model}.")

# Child class (Bike) 
class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type  # Additional attribute for Bike class

    def display_info(self):
        print(f"This is a {self.bike_type} bike: {self.brand} {self.model}.")

car = Car("Toyota", "Camry", "Sedan")
bike = Bike("Yamaha", "YZF-R3", "Sport")

car.display_info()  # Output: This is a Sedan car: Toyota Camry.
bike.display_info()  # Output: This is a Sport bike: Yamaha YZF-R3.
# Encapsulation
# **********************************************************************************************************************
class Person:
    def __init__(self, name, age):
        self.name = name       # Public attribute
        self._address = "Unknown"  # Protected attribute
        self.__age = age       # Private attribute

    def display_info(self):
        print(f"Name: {self.name}, Address: {self._address}, Age: {self.__age}")

# Create a person object
person = Person("Alice", 30)
print(person.display_info())
# disply info its show all private , public and protected attributes bcoz python allow internal access not single access
# **********************************************************************************************************************
# polymarizatiom
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an object of Calculator
calc = Calculator()

# Different ways of calling the add method
print(calc.add(5))        # Output: 5 (only one argument)
print(calc.add(5, 3))     # Output: 8 (two arguments)
print(calc.add(5, 3, 2))  # Output: 10 (three arguments)

