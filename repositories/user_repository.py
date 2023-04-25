from social_network.models.users import User
from social_network.utils.exceptions import EntityDoesNotExist


class UserRepository:
    @staticmethod
    def get_user_by_username(username):
        user = Database.get_user(username)
        if user is None:
            raise EntityDoesNotExist(f"User with username '{username}' does not exist.")
        return user

    @staticmethod
    def add_user(user):
        Database.add_user(user)

    @staticmethod
    def update_user(user):
        existing_user = Database.get_user(user.username)
        if existing_user is None:
            raise EntityDoesNotExist(f"User with username '{user.username}' does not exist.")
        Database.add_user(user)

    @staticmethod
    def delete_user(username):
        existing_user = Database.get_user(username)
        if existing_user is None:
            raise EntityDoesNotExist(f"User with username '{username}' does not exist.")
        del Database._users[username]
