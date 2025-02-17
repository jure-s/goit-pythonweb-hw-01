from abc import ABC, abstractmethod
from loguru import logger

class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model
    
    @abstractmethod
    def start_engine(self) -> None:
        """Метод для запуску двигуна"""
        pass
