from abc import ABC, abstractmethod

# Define the Serviceable interface
class Serviceable(ABC):

    @abstractmethod
    def needs_service(self)-> bool:
        pass