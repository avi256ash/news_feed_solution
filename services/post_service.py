from repositories.post_repository import PostRepository
from models.post import Post

class PostService:
    def __init__(self):
        self.post_repository = PostRepository()

    def create_post(self, post_text, author):
        post = Post(post_text, author)
        return self.post_repository.create(post)

    def get_posts(self, sort_by):
        posts = self.post_repository.get_all()
        if sort_by == "score":
            posts.sort(key=lambda x: x.score(), reverse=True)
        elif sort_by == "comments":
            posts.sort(key=lambda x: len(x.comments), reverse=True)
        elif sort_by == "timestamp":
            posts.sort(key=lambda x: x.timestamp, reverse=True)
        return posts

    def upvote_post(self, post_id, user_id):
        post = self.post_repository.get(post_id)
        if not post:
            return False
        if user_id in post.upvotes:
            return False
        if user_id in post.downvotes:
            post.downvotes.remove(user_id)
        post.upvotes.add(user_id)
        self.post_repository.update(post_id, post)
        return True

    def downvote_post(self, post_id, user_id):
        post = self.post_repository.get(post_id)
        if not post:
            return False
        if user_id in post.downvotes:
            return False
        if user_id in post.upvotes:
            post.upvotes.remove(user_id)
        post.downvotes.add(user_id)
        self.post_repository.update(post_id, post)
        return True

    def add_comment_to_post(self, post_id, comment_text, author):
        post = self.post_repository.get(post_id)
        if not post:
            return None
        comment = post.add_comment(comment_text, author)
        self.post_repository.update(post_id, post)
        return comment
