
from repositories.comment_repository import CommentRepository
from models.comment import Comment

class CommentService:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository
    
    def create_comment(self, comment_text: str, author_id: int, post_id: int):
        author = self.comment_repository.get_user_by_id(author_id)
        post = self.comment_repository.get_post_by_id(post_id)

        if not author:
            raise ValueError(f"Invalid author_id: {author_id}")
        if not post:
            raise ValueError(f"Invalid post_id: {post_id}")

        comment = Comment(comment_text, author, post)
        self.comment_repository.add_comment(comment)
        return comment

    def get_comments_by_post(self, post_id: int):
        post = self.comment_repository.get_post_by_id(post_id)
        if not post:
            raise ValueError(f"Invalid post_id: {post_id}")
        comments = self.comment_repository.get_comments_by_post(post_id)
        return comments
