from abc import ABC, abstractmethod

class IReadOnlyRepository(ABC):
    @abstractmethod
    def getAll(self): 
        raise NotImplementedError
    
    @abstractmethod
    def get(self): 
        raise NotImplementedError
