from models.UserModel import UserModel
from entities.UserEntity import User

class UserDataMapper:
    def model_to_entity(instance: UserModel) -> User:
        return User(
            user_id=instance.user_id,
            user_name=instance.username,
            password= instance.password
        )

    def entity_to_model(user: User, existing=None) -> UserModel:
        return UserModel(
            user_id=user.user_id,
            username=user.user_name,
            password=user.password,
        )