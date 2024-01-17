from tire.tire import Tire
from array import array

class OctoprimeTires(Tire):
    def __init__(self, last_service_date,sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        sum_of_values = sum(self.sensor_array)
        is_sum_greater_than_3 = sum_of_values >= 3 
        if  is_sum_greater_than_3:   
            return True
        else:
            return False