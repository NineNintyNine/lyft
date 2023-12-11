from battery.battery import Battery
from datetime import datetime, timedelta

class NubbinBattery(Battery):
    def __init__(self,last_service_date, current_date):
        self.last_service_date = last_service_date;
        self.current_date = current_date
        self.duration = timedelta(days=365 * 4)
          
    def needs_service(self)->bool:
        return self.current_date - self.last_service_date >= self.duration