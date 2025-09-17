#POLYMORPHISM VEHICLES
class Car:
    def start_engine(self):
        return "Vroom! Vroom!"

class Motorcycle:
    def start_engine(self):
        return "Brmmm Brmmm!"

class Truck:
    def start_engine(self):
        return "Rrrr! Rrrr!"
    
#INPUT VEHICLES BY USER
print ("Select a vehicle to start the engine:")
print("1. Car")
print("2. Motorcycle")
print("3. Truck")

choice = input("Enter the number of your choice: ")
if choice == '1':
    vehicle = Car()
    print(vehicle.start_engine())
elif choice == '2':
    vehicle = Motorcycle()
    print(vehicle.start_engine())
elif choice == '3':
    vehicle = Truck()
    print(vehicle.start_engine())
else:
    print("Invalid choice. Defaulting to Car.")
    vehicle = Car()
    print(vehicle.start_engine())