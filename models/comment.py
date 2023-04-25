import datetime

class Comment:
    def __init__(self, comment_text, author):
        self.comment_text = comment_text
        self.author = author
        self.timestamp = datetime.datetime.now()
        self.upvotes = set()
        self.downvotes = set()
    
    def score(self):
        return len(self.upvotes) - len(self.downvotes)
    
    def upvote(self, user):
        self.upvotes.add(user)
    
    def downvote(self, user):
        self.downvotes.add(user)
