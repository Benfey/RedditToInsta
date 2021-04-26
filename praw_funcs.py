import urllib
import time
import praw
import os

def get_posts_top(praw_object, subreddit=None, number=1):
    submission_titles = []
    submission_objects = []
    for submission in praw_object.subreddit(subreddit).top(time_filter='day', limit=number):
        if submission.stickied or submission.author.name == "AutoModerator":
            continue
        submission_objects.append(submission)
        submission_titles.append(submission.title)
    return submission_titles, submission_objects

def get_posts_hot(praw_object, subreddit=None, number=1):
    submission_titles = []
    submission_objects = []
    for submission in praw_object.subreddit(subreddit).hot(limit=10):
        if submission.stickied or submission.author.name == "AutoModerator":
            continue
        submission_objects.append(submission)
        submission_titles.append(submission.title)
        number -= 1
        if number <= 0:
            break
    return submission_titles, submission_objects

def get_comments(post_objects, number=1):
    top_comments = []
    top_comment_objects = []
    for submission in post_objects:
        submission_comments = submission.comments
        real_comments = [comment for comment in submission_comments if isinstance(comment, praw.models.Comment)]
        real_comments.sort(key=lambda comment: comment.score, reverse=True)
        top_comments.append([text.body for text in real_comments[:number]])
        top_comment_objects.append([text for text in real_comments[:number]])
    return top_comments, top_comment_objects

def reddit_instance():
    return praw.Reddit(
        client_id=os.environ['REDDIT_ID'],
        client_secret=os.environ['REDDIT_SECRET'],
        user_agent="windows:InstaBot:v0.0.1 (by /u/Sensitive-Use376)",
    )

def save_photo(post_objects):
    for post in post_objects:
        if not post.is_self:
            if any([post.url[-3:] == 'jpg', post.url[:-3] == 'png', post.url[:-4] == 'jpeg']):
                t = int(time.time())
                urllib.request.urlretrieve(post.url, f"data/pic+{t}.png")
                return f"data/pic+{t}.png"
            else:
                print("Error: not a photo")
