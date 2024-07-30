from abc import ABC, abstractmethod
class Component(ABC):
    @abstractmethod
    def operation():
        pass
    
    @abstractmethod
    def add():
        pass

    @abstractmethod
    def remove():
        pass

    @abstractmethod
    def getChild():
        pass

class Compose(Component):
    def __init__(self, name):
        self.name = name
        self.child = []

    def operation(self):
        print(f"Compose {self.name} Operation")
        for child in self.child:
            child.operation()

    def add(self, child):
        self.child.append(child)

    def remove(self, child):
        self.child.remove(child)

    def getChild(self, name):
        for child in self.child:
            if child.name == name:
                return child
        return("error")


class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        print(f"Leaf {self.name} operation")

    def add():
        print(f"Can't add to leaf")

    def getChild():
        print(f"Can't get child from leaf")

    def remove():
        print(f"Can't remove from leaf")


