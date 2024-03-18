from sqlalchemy.orm import Session
from modules.repositories.IRepository import IRepository
from modules.entities import User
from server.modules.models import UserModel
from modules.datamappers.UserDataMapper import UserDataMapper

# a sentinel value for keeping track of entities removed from the repository
REMOVED = object()

class SqlAlchemyUserRepository(IRepository):
    def __init__(self, session: Session, identity_map=None):
        self.session = session
        self._identity_map = identity_map or dict()

    def add(self, entity: User):
        self._identity_map[entity.user_id] = entity
        instance = UserDataMapper.entity_to_model(entity)
        self.session.add(instance)
        self.session.commit()  
        return instance.user_id

    def delete(self, entity: User):
        if entity.user_id in self._identity_map:
            del self._identity_map[entity.user_id]
            instance = self.session.query(UserModel).filter_by(id=entity.user_id).one()
            self.session.delete(instance)

    def get(self, id) -> User:
        if id in self._identity_map:
            return self._identity_map[id]
        else:
            instance = self.session.query(UserModel).filter_by(id=id).one()
            entity = UserDataMapper.model_to_entity(instance)
            self._identity_map[id] = entity
            return entity

    def update(self, entity: User):
        if entity.user_id in self._identity_map:
            instance = self.session.query(UserModel).filter_by(id=entity.user_id).one()
            updated_instance = UserDataMapper.entity_to_model(entity)
            for key, value in updated_instance.__dict__.items():
                setattr(instance, key, value)