from typing import List
from models.post import Post
from utils.database import Database


class PostRepository:
    @staticmethod
    def get_all_posts() -> List[Post]:
        return list(Database._posts.values())

    @staticmethod
    def get_post_by_id(post_id: str) -> Post:
        return Database.get_post(post_id)

    @staticmethod
    def add_post(post: Post):
        Database.add_post(post)

    @staticmethod
    def delete_post(post_id: str):
        post = PostRepository.get_post_by_id(post_id)
        if post:
            del Database._posts[post_id]
        else:
            raise ValueError(f"Post with id {post_id} does not exist in the database.")
