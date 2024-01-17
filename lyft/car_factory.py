from datetime import datetime, timedelta
from tokenize import Double
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tires import CarriganTires
from tire.octoprime_tires import OctoprimeTires

class CarFactory:
        @staticmethod
        # def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        #     engine = CapuletEngine(current_mileage, last_service_mileage)
        #     battery = SpindleBattery(last_service_date, current_date)
        #     return Car(engine,battery)
        def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, sensor_array: Double)-> Car:
            car = Car()
            car.engine = CapuletEngine(current_mileage, last_service_mileage)
            car.battery = SpindlerBattery(last_service_date, current_date)
            car.tire = CarriganTires(sensor_array)
            return car
        @staticmethod
        def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, sensor_array: Double)-> Car:
            car = Car()
            car.engine = WilloughbyEngine(current_mileage, last_service_mileage)
            car.battery = SpindlerBattery(last_service_date, current_date)
            car.tire = OctoprimeTires(sensor_array)
            return car
        @staticmethod
        def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool, sensor_array: Double)-> Car:
            car = Car()
            car.engine = SternmanEngine(warning_light_on)
            car.battery = SpindlerBattery(last_service_date, current_date)
            car.tire = CarriganTires(sensor_array)
            return car
        @staticmethod
        def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, sensor_array: Double)-> Car:
            car = Car()
            car.engine = WilloughbyEngine(current_mileage, last_service_mileage)
            car.battery = NubbinBattery(last_service_date, current_date)
            car.tire = OctoprimeTires(sensor_array)
            return car
        @staticmethod
        def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, sensor_array: Double)-> Car:
            car = Car()
            car.engine = CapuletEngine(current_mileage, last_service_mileage)
            car.battery = NubbinBattery(last_service_date, current_date)
            car.tire = CarriganTires(sensor_array)
            return car
        @staticmethod
        def needs_service(car:Car)->bool:
            return car.needs_service()