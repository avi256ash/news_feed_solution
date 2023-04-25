from repositories.user_repository import UserRepository
from models.user import User

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def signup(self, username: str, password: str) -> User:
        user = User(username=username, password=password)
        return self.user_repository.add_user(user)

    def login(self, username: str, password: str) -> User:
        user = self.user_repository.get_user_by_username(username)
        if user is None or user.password != password:
            return None
        return user

    def follow(self, follower_username: str, following_username: str) -> bool:
        follower = self.user_repository.get_user_by_username(follower_username)
        following = self.user_repository.get_user_by_username(following_username)
        if follower is None or following is None:
            return False
        return self.user_repository.add_following(follower, following)

    def unfollow(self, follower_username: str, following_username: str) -> bool:
        follower = self.user_repository.get_user_by_username(follower_username)
        following = self.user_repository.get_user_by_username(following_username)
        if follower is None or following is None:
            return False
        return self.user_repository.remove_following(follower, following)
