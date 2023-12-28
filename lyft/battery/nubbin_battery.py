from battery.battery import Battery
from datetime import datetime, timedelta
from utils import add_years_to_date

class NubbinBattery(Battery):
    def __init__(self,last_service_date, current_date):
        self.last_service_date = last_service_date;
        self.current_date = current_date
        # self.duration = timedelta(days=365 * 4)
          
    def needs_service(self)->bool:
        duration = add_years_to_date(self.last_service_date,4)
        return duration < self.current_date
    