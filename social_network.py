class SocialNetwork:
    def __init__(self):
        self.users = {}
        self.current_user = None
    
    def signup(self, username, password):
        if username in self.users:
            print("Username already taken")
            return
        
        user = User(username, password)
        self.users[username] = user
        print(f"User {username} signed up")
    
    def login(self, username, password):
        if username not in self.users:
            print("User does not exist")
            return
        
        user = self.users[username]
        if user.password != password:
            print("Incorrect password")
            return
        
        self.current_user = user
        print(f"User {username} logged in")
    
    def post(self, post_text):
        if not self.current_user:
            print("Please login first")
            return
        
        post = self.current_user.post(post_text)
        print(f"Post {post.post_text} created")
    
    def follow(self, username):
        if not self.current_user:
            print("Please login first")
            return
        
        if username not in self.users:
            print("User does not exist")
            return
        
        user = self.users[username]
        self.current_user.follow(user)
        print(f"You are now following {username}")
    
    def unfollow(self, username):
        if not self.current_user:
            print("Please login first")
            return
        
        if username not in self.users:
            print("User does not exist")
            return
        
        user = self.users[username]
        self.current_user.unfollow(user)
        print(f"You are no longer following {username}")
    
    def view_feed(self, sort_by):
        if not self.current_user:
            print("Please login first")
            return
        
        feed = self.current_user.get_feed(sort_by)
        for post in feed:
            print(f"{post.post_text} - {post.author.username}")
            print(f"Score: {post.score()} | Comments: {len(post.comments)} | Timestamp: {post.timestamp}")
            print("Comments:")
            for comment in post.comments:
                print(f"{comment.comment_text} - {comment.author.username}")
                print(f"Score: {comment.score()} | Timestamp: {comment.timestamp}")
            print("--------------------")
    
    def upvote_post(self, post_id):
        if not self.current_user:
            print("Please login first")
            return
        
        for user in self.users.values():
            for post in user.posts:
                if post_id == id(post):
                    post.upvote(self.current_user)
                    print(f"{self.current_user.username} upvoted the post")
                    return
        
        print("Post not found")
    
    def downvote_post(self, post_id):
        if not self.current_user:
            print("Please login first")
            return
        
        for user in self.users.values():
            for post in user.posts:
                if post_id == id(post):
                    post.downvote(self.current_user)
                    print(f"{self.current_user.username} downvoted the post")
                    return
        
        print("Post not found")
    
    def comment_on_post(self, post_id, comment_text):
        if not self.current_user:
            print("Please login first")
            return
        
        for user in self.users.values():
            for post in user.posts:
                if post_id == id(post):
                    comment = post.add_comment(comment_text, self.current_user.username)
                    print(f"Comment {comment.comment_text} added to the post")
                    return
        
        print("Post not found")
    
    def upvote_post(self, post_index):
        if not self.current_user:
            print("Please login first")
            return
        
        try:
            post = self.current_user.posts[post_index]
        except IndexError:
            print("Invalid post index")
            return
        
        post.upvote(self.current_user)
        print("Post upvoted")
    
    def downvote_post(self, post_index):
        if not self.current_user:
            print("Please login first")
            return
        
        try:
            post = self.current_user.posts[post_index]
        except IndexError:
            print("Invalid post index")
            return
        
        post.downvote(self.current_user)
        print("Post downvoted")
    
    def comment(self, post_index, comment_text):
        if not self.current_user:
            print("Please login first")
            return
        
        try:
            post = self.current_user.posts[post_index]
        except IndexError:
            print("Invalid post index")
            return
        
        comment = post.add_comment(comment_text, self.current_user.username)
        print(f"Comment {comment.comment_text} added to post {post.post_text}")
    
    def upvote_comment(self, post_index, comment_index):
        if not self.current_user:
            print("Please login first")
            return
        
        try:
            post = self.current_user.posts[post_index]
            comment = post.comments[comment_index]
        except (IndexError, AttributeError):
            print("Invalid post or comment index")
            return
        
        comment.upvote(self.current_user)
        print("Comment upvoted")
    
    def downvote_comment(self, post_index, comment_index):
        if not self.current_user:
            print("Please login first")
            return
        
        try:
            post = self.current_user.posts[post_index]
            comment = post.comments[comment_index]
        except (IndexError, AttributeError):
            print("Invalid post or comment index")
            return
        
        comment.downvote(self.current_user)
        print("Comment downvoted")
    
    def get_feed(self, sort_by):
        if not self.current_user:
            print("Please login first")
            return
        
        feed = self.current_user.get_feed(sort_by)
        
        print("Your feed:")
        for post in feed:
            print(f"Post: {post.post_text} | Author: {post.author} | Upvotes: {len(post.upvotes)} | Downvotes: {len(post.downvotes)} | Comments: {len(post.comments)}")
            for comment in post.comments:
                print(f"    Comment: {comment.comment_text} | Author: {comment.author} | Upvotes: {len(comment.upvotes)} | Downvotes: {len(comment.downvotes)}")
    
    def logout(self):
        self.current_user = None
        print("You have been logged out")
