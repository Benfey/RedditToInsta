from praw_funcs import *
from insta import *

if __name__ == "__main__":

    reddit = reddit_instance()

    subreddit = "funny"
    post_titles, post_objects = get_posts_hot(reddit, subreddit)
    post_comments, post_comments_objects = get_comments(post_objects)

    upload_photo(save_photo(post_objects), f'"{post_titles[0]}" - /u/{post_objects[0].author}')
