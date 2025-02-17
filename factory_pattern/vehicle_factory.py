from abc import ABC, abstractmethod
from .vehicle import Vehicle

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        """Створює екземпляр автомобіля"""
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        """Створює екземпляр мотоцикла"""
        pass
