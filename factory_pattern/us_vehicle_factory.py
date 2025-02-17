from .vehicle_factory import VehicleFactory
from .car import Car
from .motorcycle import Motorcycle
from .vehicle import Vehicle

class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(f"{make} (US Spec)", model)

# Тестуємо фабрику
if __name__ == "__main__":
    factory = USVehicleFactory()
    car = factory.create_car("Ford", "Mustang")
    motorcycle = factory.create_motorcycle("Harley-Davidson", "Sportster")
    
    car.start_engine()
    motorcycle.start_engine()