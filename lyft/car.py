from abc import abstractmethod
from serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery
from tire.tire import Tire

# class Car(Serviceable):
#     def __init__(self,engine,battery):
#         self.engine = engine
#         self.battery = battery    

class Car(  Serviceable):
    def __init__(self):
        self.engine = Engine()
        self.battery = Battery()  
        self.tire = Tire()
    def needs_service(self)->bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
