from sqlalchemy.orm import Session
from repositories.IRepository import IRepository
from entities.UserEntity import User
from models.UserModel import UserModel
from datamappers.UserDataMapper import UserDataMapper

# a sentinel value for keeping track of entities removed from the repository
REMOVED = object()

class SqlAlchemyFlashCardRepository(IRepository):
    """SqlAlchemy implementation of ListingRepository"""

    def __init__(self, session: Session, identity_map=None):
        self.session = session
        self._identity_map = identity_map or dict()

    def add(self, entity: User):
        self._identity_map[entity.user_id] = entity
        instance = UserDataMapper.entity_to_model(entity)
        self.session.add(instance)
    
    def delete(self, entity: User):
        """Removes existing entity from a repository"""
        raise NotImplementedError()

    def get(id) -> User:
        raise NotImplementedError()

    def update(self): 
        raise NotImplementedError