from abc import ABC, abstractmethod

class Chain(ABC):
    @abstractmethod
    def operation():
        pass
    
    @abstractmethod
    def add_chain():
        pass


class ResponsabilityOne(Chain):
    def __init__(self):
        self.next: Chain = None

    def operation(self):
        print('res 1 operation')
        self.next.operation()

    def add_chain(self, next: Chain):
        self.next = next

class FinalResponsability(Chain):
    def __init__(self):
        self.next: Chain = None
    
    def operation():
        print('res 2 operation')
    
    def add_chain(self, next: Chain):
        self.next = next
        
    