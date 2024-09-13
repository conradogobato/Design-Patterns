from abc import ABC, abstractmethod

class Constructor(ABC):
    @abstractmethod
    def build_one():
        pass
    def build_two():
        pass

class Client():
    def __init__(self, constructor: Constructor) -> None:
        self.constructor = constructor     

    def build(self):
        self.constructor.build_one()
        self.constructor.build_two   

