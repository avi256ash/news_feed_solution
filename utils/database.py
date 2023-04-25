class Database:
    _users = {}
    _posts = {}
    _comments = {}

    @staticmethod
    def get_user(username):
        return Database._users.get(username)

    @staticmethod
    def add_user(user):
        Database._users[user.username] = user

    @staticmethod
    def get_post(post_id):
        return Database._posts.get(post_id)

    @staticmethod
    def add_post(post):
        Database._posts[post.post_id] = post

    @staticmethod
    def get_comment(comment_id):
        return Database._comments.get(comment_id)

    @staticmethod
    def add_comment(comment):
        Database._comments[comment.comment_id] = comment
