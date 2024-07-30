from abc import ABC, abstractmethod

class Alvo:
    def __init__(self, nome):
        self.nome = nome

    def operation(self):
        print(self.nome)

class Adapter(Alvo):
    def __init__(self, adaptee):
        super().__init__
        self.adaptee = adaptee
    
    def operation(self):
        return self.adaptee.operation()
    
class ClassToAdapt:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def operation(self):
        print(f'{self.nome} {self.sobrenome}')