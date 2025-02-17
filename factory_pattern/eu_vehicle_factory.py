from .vehicle_factory import VehicleFactory
from .car import Car
from .motorcycle import Motorcycle
from .vehicle import Vehicle

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(f"{make} (EU Spec)", model)

# Тестуємо фабрику
if __name__ == "__main__":
    factory = EUVehicleFactory()
    car = factory.create_car("BMW", "320i")
    motorcycle = factory.create_motorcycle("Ducati", "Panigale")
    
    car.start_engine()
    motorcycle.start_engine()