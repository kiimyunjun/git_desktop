from abc import ABC,abstractmethod

class ShowData(ABC):
    @abstractmethod
    def show_data(self):
        pass