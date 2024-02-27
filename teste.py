from abc import ABC, abstractmethod
class Coisa(ABC):
    def __init__(self) -> None:
        print("Coisou")
    
    @abstractmethod
    def testante(self):
        pass
    
class Computado(Coisa):
    def __init__(self) -> None:
        super().__init__()

    def testante(self):
        print("Oba testo")

a = Computado()
a.testante()