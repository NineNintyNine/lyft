from battery.battery import Battery
from datetime import datetime, timedelta
from utils import add_years_to_date

class SpindleBattery(Battery):
    def __init__(self,last_service_date, current_date):
        self.last_service_date = last_service_date;
        self.current_date = current_date
        
    def needs_service(self)->bool:
            duration = add_years_to_date(self.last_service_date,3)
            return duration < self.current_date
    
