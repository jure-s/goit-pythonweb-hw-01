from .vehicle import Vehicle
from loguru import logger

class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")

# Тестуємо клас
if __name__ == "__main__":
    car = Car("Toyota", "Corolla")
    car.start_engine()