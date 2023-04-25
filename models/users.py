import datetime

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.following = set()
        self.posts = []

    def post(self, post_text: str):
        post = Post(post_text, self.username)
        self.posts.append(post)
        return post

    def follow(self, other_user):
        self.following.add(other_user)

    def unfollow(self, other_user):
        self.following.remove(other_user)

    def get_feed(self, sort_by: str):
        feed = []
        for user in self.following:
            feed.extend(user.posts)
        feed.extend(self.posts)

        if sort_by == "score":
            feed.sort(key=lambda x: x.score(), reverse=True)
        elif sort_by == "comments":
            feed.sort(key=lambda x: len(x.comments), reverse=True)
        elif sort_by == "timestamp":
            feed.sort(key=lambda x: x.timestamp, reverse=True)

        return feed
