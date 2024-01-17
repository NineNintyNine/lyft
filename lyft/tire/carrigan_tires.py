from tire.tire import Tire
from array import array

class CarriganTires(Tire):
    def __init__(self,sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        has_value_greater_than_0_9_or_equal = any(value >= 0.9 for value in self.sensor_array)
        if has_value_greater_than_0_9_or_equal:
            return True
        else:
            return False