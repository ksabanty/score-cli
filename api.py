import requests
import requests.auth
import config
import praw
import pandas as pd


def request(sub):
    user_agent = "Score CLI by notaburner0"
    reddit = praw.Reddit(username=config.reddit_user, password=config.reddit_pw, client_id=config.client_id, client_secret=config.client_secret, user_agent=user_agent)

    sub = reddit.subreddit(sub)

    return sub
