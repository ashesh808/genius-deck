from server.modules.models import UserModel
from entities import User
from datamappers.IDataMapper import IDataMapper

class UserDataMapper(IDataMapper):
    def model_to_entity(self, instance: UserModel) -> User:
        return User(
            user_id=instance.user_id,
            user_name=instance.username,
            password=instance.password
        )

    def entity_to_model(self, user: User, existing=None) -> UserModel:
        if existing:
            # Update the existing model instance
            existing.user_id = user.user_id
            existing.username = user.user_name
            existing.password = user.password
            return existing
        else:
            # Create a new model instance
            return UserModel(
                user_id=user.user_id,
                username=user.user_name,
                password=user.password,
            )