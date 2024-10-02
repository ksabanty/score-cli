import requests
import requests.auth
import config
import praw
import pandas as pd

#client_auth = requests.auth.HTTPBasicAuth(config.client_id, config.client_secret)
#post_data = {f"grant_type": "password", "username": config.reddit_user, "password": config.reddit_pw}
#headers = {"User-Agent": "Score CLI by notaburner0"}

#response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

#auth_res = response.json()
#access_token = auth_res['access_token']

user_agent = "Score CLI by notaburner0"
reddit = praw.Reddit(username=config.reddit_user, password=config.reddit_pw, client_id=config.client_id, client_secret=config.client_secret, user_agent=user_agent)

sub_name = "soccer"
sub = reddit.subreddit(sub_name)
#print(sub.display_name)

df = pd.DataFrame()

titles = []
links = []

for post in sub.new(limit=20):
    if post.link_flair_text == 'Media':
        titles.append(post.title)
        links.append(post.url_overridden_by_dest)

#print(vars(post))
df['Title'] = titles
df['Link'] = links

print(df.to_string())
