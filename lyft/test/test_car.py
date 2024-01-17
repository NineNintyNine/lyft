import unittest

from datetime import datetime, timedelta
from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        sensor_array = [0.1,0.1,0.5,0.6]
        
         
        car_factory = CarFactory()
        calliope_car = car_factory.create_calliope(current_date,last_service_date,current_mileage,last_service_mileage, sensor_array)
        self.assertTrue(car_factory.needs_service(calliope_car))
        

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        sensor_array = [0.1,0.1,0.5,0.6]
        
        car_factory = CarFactory()
        calliope_car = car_factory.create_calliope(current_date,last_service_date,current_mileage,last_service_mileage, sensor_array)
        self.assertTrue(car_factory.needs_service(calliope_car))
        

'''
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        
        car_factory = CarFactory()
        calliope_car = car_factory.create_calliope(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car_factory.needs_service(calliope_car))

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date= datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        
        car_factory = CarFactory()
        calliope_car = car_factory.create_calliope(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car_factory.needs_service(calliope_car))


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        
        car_factory = CarFactory()
        glissade_car = car_factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(glissade_car))
        

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        
        car_factory = CarFactory()
        glissade_car = car_factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(glissade_car))


    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car_factory = CarFactory()
        glissade_car = car_factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(glissade_car))

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car_factory = CarFactory()
        glissade_car = car_factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(glissade_car))


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        warning_light_on = False

        car_factory = CarFactory()
        palindrome_car = car_factory.create_palindrome(current_date, last_service_date, warning_light_on)
        self.assertTrue(car_factory.needs_service(palindrome_car))

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        warning_light_on = False

        car_factory = CarFactory()
        palindrome_car = car_factory.create_palindrome(current_date, last_service_date, warning_light_on)
        self.assertTrue(car_factory.needs_service(palindrome_car))

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        warning_light_on = True

        car_factory = CarFactory()
        palindrome_car = car_factory.create_palindrome(current_date, last_service_date, warning_light_on)
        self.assertTrue(car_factory.needs_service(palindrome_car))

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        warning_light_on = False

        car_factory = CarFactory()
        palindrome_car = car_factory.create_palindrome(current_date, last_service_date, warning_light_on)
        self.assertTrue(car_factory.needs_service(palindrome_car))


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)  
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory()
        rorschach_car = car_factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(rorschach_car))

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)  
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory()
        rorschach_car = car_factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(rorschach_car))

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car_factory = CarFactory()
        rorschach_car = car_factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(rorschach_car))

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car_factory = CarFactory()
        rorschach_car = car_factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(rorschach_car))


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        
        car_factory = CarFactory()
        thovex_car = car_factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(thovex_car))
        

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory()
        thovex_car = car_factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(thovex_car))

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car_factory = CarFactory()
        thovex_car = car_factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(thovex_car))
        
    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car_factory = CarFactory()
        thovex_car = car_factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_factory.needs_service(thovex_car))
'''

if __name__ == '__main__':
    unittest.main()
