from .vehicle import Vehicle
from loguru import logger

class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")

# Тестуємо клас
if __name__ == "__main__":
    motorcycle = Motorcycle("Harley-Davidson", "Sportster")
    motorcycle.start_engine()