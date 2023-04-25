import datetime
from comment import Comment


class Post:
    def __init__(self, post_text, author):
        self.post_text = post_text
        self.author = author
        self.timestamp = datetime.datetime.now()
        self.upvotes = set()
        self.downvotes = set()
        self.comments = []

    def score(self):
        return len(self.upvotes) - len(self.downvotes)

    def upvote(self, user):
        self.upvotes.add(user)

    def downvote(self, user):
        self.downvotes.add(user)

    def add_comment(self, comment_text, author):
        comment = Comment(comment_text, author)
        self.comments.append(comment)
        return comment
