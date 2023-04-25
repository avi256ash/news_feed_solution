import argparse

from social_network import SocialNetwork


def main():
    parser = argparse.ArgumentParser(description='Social Network CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Subcommand to signup a new user
    signup_parser = subparsers.add_parser('signup')
    signup_parser.add_argument('username', type=str, help='Username for new user')
    signup_parser.add_argument('password', type=str, help='Password for new user')

    # Subcommand to login as an existing user
    login_parser = subparsers.add_parser('login')
    login_parser.add_argument('username', type=str, help='Username of existing user')
    login_parser.add_argument('password', type=str, help='Password of existing user')

    # Subcommand to create a new post
    post_parser = subparsers.add_parser('post')
    post_parser.add_argument('post_text', type=str, help='Text of the post')

    # Subcommand to follow another user
    follow_parser = subparsers.add_parser('follow')
    follow_parser.add_argument('username', type=str, help='Username of user to follow')

    # Subcommand to unfollow another user
    unfollow_parser = subparsers.add_parser('unfollow')
    unfollow_parser.add_argument('username', type=str, help='Username of user to unfollow')

    # Subcommand to get the user's feed
    feed_parser = subparsers.add_parser('feed')
    feed_parser.add_argument('sort_by', type=str, help='Sort order for feed: score, comments, or timestamp')

    args = parser.parse_args()

    # Create Social Network object
    social_network = SocialNetwork()

    # Dispatch to appropriate method based on command
    if args.command == 'signup':
        social_network.signup(args.username, args.password)
    elif args.command == 'login':
        social_network.login(args.username, args.password)
    elif args.command == 'post':
        social_network.post(args.post_text)
    elif args.command == 'follow':
        social_network.follow(args.username)
    elif args.command == 'unfollow':
        social_network.unfollow(args.username)
    elif args.command == 'feed':
        social_network.get_feed(args.sort_by)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
