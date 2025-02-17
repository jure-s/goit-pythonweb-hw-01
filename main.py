from factory_pattern.us_vehicle_factory import USVehicleFactory
from factory_pattern.eu_vehicle_factory import EUVehicleFactory

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
            print("Невірний вибір. Спробуйте ще раз.")
            continue

        car = factory.create_car("Ford", "Mustang")
        motorcycle = factory.create_motorcycle("Harley-Davidson", "Sportster")
        
        car.start_engine()
        motorcycle.start_engine()

def main():
    while True:
        print("Оберіть програму для запуску:")
        print("1 - Фабричний патерн (Factory Pattern)")
        print("0 - Вихід")
        
        option = input("Ваш вибір: ").strip()
        
        if option == "0":
            print("Програма завершена.")
            break
        elif option == "1":
            run_factory_pattern()
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()