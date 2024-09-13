class Memento():
    def __init__(self, estado) -> None:
        self.estado = estado
    
    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado


class Fonte():
    def __init__(self, estado) -> None:
        self.estado = estado

    def createMemento(self):
        return(Memento(self.estado))
    
    def setMemento(self, memento: Memento):
        self.estado = memento.getEstado()


