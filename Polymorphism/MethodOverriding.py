class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Car(Vehicle):
    def start(self):
        print("Starting car...")

class Bike(Vehicle):
    def start(self):
        print("Starting bike...")

class Bus(Vehicle):
    def stop(self):
        print("stop my Bus...")

vehicles = [Car(), Bike() , Bus()]
print(type(vehicles))
for v in vehicles:
    v.start()  # Polymorphic behavior
