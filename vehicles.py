# Base Vehicle class (Assignment 1)
class Vehicle:
    def __init__(self, brand, speed):
        self._brand = brand  # Encapsulated attribute
        self._speed = speed  # Encapsulated attribute

    # Getter for brand (encapsulation)
    @property
    def brand(self):
        return self._brand

    # Method to be overridden by subclasses (for polymorphism)
    def move(self):
        raise NotImplementedError("Subclass must implement move method")

    # Common method for all vehicles
    def info(self):
        return f"Brand: {self._brand}, Speed: {self._speed} km/h"

# Car class inheriting from Vehicle (Assignment 2)
class Car(Vehicle):
    def move(self):
        return f"{self._brand} is driving on the road! 🚗"

# Plane class inheriting from Vehicle (Assignment 2)
class Plane(Vehicle):
    def move(self):
        return f"{self._brand} is flying in the sky! ✈️"

# Main program to demonstrate both assignments
def main():
    # Create vehicle instances
    car = Car("Toyota", 120)
    plane = Plane("Boeing", 900)

    # List for polymorphic behavior
    vehicles = [car, plane]

    # Demonstrate polymorphism with move (Assignment 2)
    print("Vehicles in action:")
    for vehicle in vehicles:
        print(vehicle.move())

    # Demonstrate vehicle info (Assignment 1)
    print("\nVehicle details:")
    for vehicle in vehicles:
        print(vehicle.info())

if __name__ == "__main__":
    main()
