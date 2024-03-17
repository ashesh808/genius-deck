from abc import abstractmethod
from modules.repositories.IReadOnlyRepository import IReadOnlyRepository

class IRepository(IReadOnlyRepository):
    @abstractmethod 
    def add(self):
        raise NotImplementedError 

    @abstractmethod
    def delete(self): 
        raise NotImplementedError
    
    @abstractmethod
    def update(self): 
        raise NotImplementedError