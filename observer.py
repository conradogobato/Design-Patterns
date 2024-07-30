from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Subject:
    def __init__(self):
        self._observers : list[Observer] = []
    
    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class ConcreteObserver(Observer):
    def __init__(self, nome):
        self.nome = nome

    def update(self):
        print(f'Observer {self.nome} recceived the message')


obs1 = ConcreteObserver('Claudio')
obs2 = ConcreteObserver('Roberto')

subject = Subject()
subject.add_observer(obs1)
subject.add_observer(obs2)

subject.notify()