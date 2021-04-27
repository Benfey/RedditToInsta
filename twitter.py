import tweepy
import os

def tweet(photo, caption):

    auth = tweepy.OAuthHandler(os.environ['TWITTER_API'], os.environ['TWITTER_API_SECRET'])
    auth.set_access_token(os.environ['TWITTER_ACCESS'], os.environ['TWITTER_ACCESS_SECRET'])
    api = tweepy.API(auth)

     # Upload image
    media = api.media_upload(photo)

    status = api.update_status(status=caption, media_ids=[media.media_id])
