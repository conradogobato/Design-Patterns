class Mediator:
    def __init__(self, mediator):
        self.mediator = mediator

    def mediated_operation(self):
        self.mediator.operation()

class ConcreteMediator:
    def __init__(self, cOne, cTwo):
        self.cOne = cOne
        self.cTwo = cTwo
    
    def operation(self):
        self.cOne.operation()
        self.cTwo.operation()

class CollaboratorOne:
    def operation(self):
        print('Operation 1')

class CollaboratorTwo:
    def operation(self):
        print('Operation 2')