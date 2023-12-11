# from datetime import date,datetime
# from car_factory import CarFactory

# def main():
#     # Creating an instance of CarFactory
#     car_factory = CarFactory()

#     # Creating different types of cars using the factory methods
#     calliope_car = car_factory.create_calliope(current_date=datetime(2023, 1, 1), last_service_date=datetime(2022, 12, 28), current_mileage=5000, last_service_mileage=4500)

#     # Checking if the cars need service
#     print("Calliope Car needs service:", calliope_car.needs_service())

# if __name__ == "__main__":
#     main()

from datetime import date, datetime
from car_factory import CarFactory

def main():
    # Example usage of CarFactory
        car_factory = CarFactory()
        calliope_car = car_factory.create_calliope(
        current_date=date.today(),
        last_service_date=date(2022, 12, 28),
        current_mileage=5000,
        last_service_mileage=4500
    )
        palindrome_car =car_factory.create_palindrome(
             current_date=date.today(), 
             last_service_date = date(2019, 12, 28), 
             warning_light_on = False
    )

    # Check if the car needs service
        if car_factory.needs_service(calliope_car):
            print("The car needs service.")
        else:
            print("The car does not need service.")
        

        if car_factory.needs_service(palindrome_car):
            print("The car needs service.")
        else:
            print("The car does not need service.")

if __name__ == "__main__":
    main()

