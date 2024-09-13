from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone():
        pass


class ConcretePrototype(Prototype):
    def __init__(self, name) -> None:
        self.name = name

    def clone(self):
        return copy.deepcopy(self)