from abc import ABC, abstractmethod

class IReadOnlyRepository(ABC):
    @abstractmethod
    def get(self): 
        raise NotImplementedError
