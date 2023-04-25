from typing import List
from models.comment import Comment
from utils.database import Database


class CommentRepository:
    @staticmethod
    def get_comment_by_id(comment_id: str) -> Comment:
        return Database.get_comment(comment_id)

    @staticmethod
    def add_comment(comment: Comment) -> None:
        Database.add_comment(comment)

    @staticmethod
    def update_comment(comment_id: str, new_content: str) -> None:
        comment = CommentRepository.get_comment_by_id(comment_id)
        if comment:
            comment.content = new_content

    @staticmethod
    def delete_comment(comment_id: str) -> None:
        comment = CommentRepository.get_comment_by_id(comment_id)
        if comment:
            post = comment.post
            post.comments.remove(comment)
            del Database._comments[comment_id]

    @staticmethod
    def get_comments_for_post(post_id: str) -> List[Comment]:
        post_comments = []
        for comment in Database._comments.values():
            if comment.post.post_id == post_id:
                post_comments.append(comment)
        return post_comments
