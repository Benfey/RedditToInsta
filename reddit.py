from praw_funcs import *
from twitter import *
import datetime
import random
import time
import os

if __name__ == "__main__":

    reddit = reddit_instance()

    subreddits = ["funny",
                "nocontextpics",
                "interestingasfuck",
                "aww",
                "Wellthatsucks",
                "Earthporn",
                "BikiniBottomTwitter",
                "hmmm",
                "OSHA"]

    random.shuffle(subreddits)

    serious = ["nocontextpics", "interestingasfuck", "Earthporn"]

    for i in range(len(subreddits)):

        post_titles, post_objects = get_posts_hot(reddit, subreddits[i])
        post_comments, post_comments_objects = get_comments(post_objects)

        if (photo := save_photo(post_objects)) == False:
            print(f"Post on {subreddits[i]} was not a photo.\n{reddit.config.reddit_url + post_objects[0].permalink}")
            continue

        if any([sub == subreddits[i] for sub in serious]):
            caption = f'"{post_titles[0]}"\n\nPost author: /u/{post_objects[0].author}\nr/{subreddits[i]}\n\nLink: {reddit.config.reddit_url + post_objects[0].permalink}\n#{subreddits[i]} #reddit #pics #amazing #cool'
        else:
            caption = f'"{post_titles[0]}"\n\nPost author: /u/{post_objects[0].author}\nr/{subreddits[i]}\n\nLink: {reddit.config.reddit_url + post_objects[0].permalink}\n#{subreddits[i]} #reddit #pics #memes'

        print(f"Posted from {subreddits[i]}")
        tweet(photo, caption)
        time.sleep(300)

    for _, _, files in os.walk("data/"):
        for file in files:
            os.remove(f"data/{file}")
