import pytest
from factory_pattern.us_vehicle_factory import USVehicleFactory
from factory_pattern.eu_vehicle_factory import EUVehicleFactory
from factory_pattern.vehicle import Vehicle

def test_us_vehicle_factory():
    factory = USVehicleFactory()
    car = factory.create_car("Ford", "Mustang")
    motorcycle = factory.create_motorcycle("Harley-Davidson", "Sportster")
    
    assert isinstance(car, Vehicle)
    assert isinstance(motorcycle, Vehicle)
    assert car.make == "Ford (US Spec)"
    assert motorcycle.make == "Harley-Davidson (US Spec)"

def test_eu_vehicle_factory():
    factory = EUVehicleFactory()
    car = factory.create_car("BMW", "320i")
    motorcycle = factory.create_motorcycle("Ducati", "Panigale")
    
    assert isinstance(car, Vehicle)
    assert isinstance(motorcycle, Vehicle)
    assert car.make == "BMW (EU Spec)"
    assert motorcycle.make == "Ducati (EU Spec)"

if __name__ == "__main__":
    pytest.main()