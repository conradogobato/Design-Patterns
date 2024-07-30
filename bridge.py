from abc import ABC, abstractmethod

class Impl(ABC):
    @abstractmethod
    def getDados(self, type):
        pass

class Publicacao:
    def __init__(self, impl: Impl):
        self.impl = impl

    def getDados(self, type):
        return self.impl.getDados(type)

    def getAutor(self):
        pass

    def getTitulo(self):
        pass

class Livro(Publicacao):
    def __init__(self, impl: Impl, title, id, content, autor):
        super().__init__(impl)
        self.id = id
        self.title = title
        self.content = content
        self.autor = autor

    def getISBN(self):
        return self.content
    
    def getTitle(self):
        return self.title

    def getAutor(self):
        return self.autor
    
class Revista(Publicacao):
    def __init__(self, impl: Impl, title, id, content, autor):
        super().__init__(impl)
        self.id = id
        self.title = title
        self.content = content
        self.autor = autor

    def getArticle(self):
        return self.content
    
    def getTitle(self):
        return self.title

    def getAutor(self):
        return self.autor


class ImplBD(Impl):
    def getDados(self, type):
        return 'Database impl'
    
class ImplXML(Impl):
    def getDados(self, type):
        return 'XML impl'


