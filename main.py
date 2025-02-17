from factory_pattern.us_vehicle_factory import USVehicleFactory
from factory_pattern.eu_vehicle_factory import EUVehicleFactory
from solid_library.library_manager import LibraryManager
from solid_library.library import Library

from loguru import logger

def run_factory_pattern():
    """Запуск фабричного патерну для створення транспортних засобів"""
    while True:
        print("Оберіть регіон: (1) US, (2) EU, (0) Вихід")
        choice = input("Ваш вибір: ").strip()
        
        if choice == "0":
            return
        elif choice == "1":
            factory = USVehicleFactory()
        elif choice == "2":
            factory = EUVehicleFactory()
        else:
            logger.warning(f"Невірний вибір: {choice}")
            print("Спробуйте ще раз.")
            continue

        car = factory.create_car("Ford", "Mustang")
        motorcycle = factory.create_motorcycle("Harley-Davidson", "Sportster")
        
        car.start_engine()
        motorcycle.start_engine()

def run_solid_library():
    """Запуск бібліотечної системи"""
    library = Library()
    manager = LibraryManager(library)
    
    while True:
        print("Оберіть дію: (1) Додати книгу, (2) Видалити книгу, (3) Показати книги, (0) Вихід")
        command = input("Ваш вибір: ").strip()
        
        if command == "0":
            return
        elif command == "1":
            title = input("Введіть назву книги: ").strip()
            author = input("Введіть автора книги: ").strip()
            year = input("Введіть рік видання: ").strip()
            
            if not year.isdigit():
                logger.warning("Невірний формат року.")
                print("Рік має бути числом. Спробуйте ще раз.")
                continue
            
            manager.add_book(title, author, int(year))
        elif command == "2":
            title = input("Введіть назву книги для видалення: ").strip()
            manager.remove_book(title)
        elif command == "3":
            manager.show_books()
        else:
            logger.warning(f"Невірний вибір: {command}")
            print("Спробуйте ще раз.")

def main():
    while True:
        print("Оберіть програму для запуску:")
        print("1 - Фабричний патерн (Factory Pattern)")
        print("2 - Бібліотека (SOLID)")
        print("0 - Вихід")
        
        option = input("Ваш вибір: ").strip()
        
        if option == "0":
            logger.info("Програма завершена користувачем.")
            break
        elif option == "1":
            run_factory_pattern()
        elif option == "2":
            run_solid_library()
        else:
            logger.warning(f"Невірний вибір: {option}")
            print("Спробуйте ще раз.")

if __name__ == "__main__":
    main()