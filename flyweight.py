from abc import ABC, abstractmethod

class FlyWeight(ABC):
    @abstractmethod
    def operacao(self, estado):
        pass


class FlyWeightConcreto(FlyWeight):
    def operacao(self, estado):
        print("FlyWeightConcreto: operação com estado " + estado)


class FlyWeightFactory:
    def __init__(self):
        self.flyWeightPool = dict()

    def getFlyWeight(self, id: int):
        if id in self.flyWeightPool:
            return self.flyWeightPool[id]
        else:
            newFlyWeight = FlyWeightConcreto()
            self.flyWeightPool[id] = newFlyWeight
            return newFlyWeight
