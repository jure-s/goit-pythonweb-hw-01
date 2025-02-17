# goit-pythonweb-hw-01

c:\Projects\goit-pythonweb-hw-01\
│
├── factory_pattern\
│   ├── __init__.py
│   ├── vehicle.py          # Базовий клас Vehicle
│   ├── car.py              # Клас Car
│   ├── motorcycle.py       # Клас Motorcycle
│   ├── vehicle_factory.py  # Абстрактний клас VehicleFactory
│   ├── us_vehicle_factory.py # Фабрика для US Spec
│   ├── eu_vehicle_factory.py # Фабрика для EU Spec
│
├── solid_library\
│   ├── __init__.py
│   ├── book.py             # Клас Book
│   ├── library_interface.py # Інтерфейс LibraryInterface
│   ├── library.py          # Реалізація бібліотеки
│   ├── library_manager.py  # Клас LibraryManager
│
├── tests\
│   ├── factory_tests.py    # Тести для фабричного патерну
│   ├── library_tests.py    # Тести для SOLID бібліотеки
│
├── .gitignore
├── requirements.txt        # Список необхідних бібліотек (`black`, `mypy`, `pytest`, `loguru`)
├── README.md               # Опис проєкту та інструкції
├── main.py                 # Головний файл для запуску обраного модуля
