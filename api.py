import requests
import requests.auth
import config

client_auth = requests.auth.HTTPBasicAuth(config.client_id, config.client_secret)
post_data = {f"grant_type": "password", "username": config.reddit_user, "password": config.reddit_pw}
headers = {"User-Agent": "Score CLI by notaburner0"}

response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

auth_res = response.json()
access_token = auth_res['access_token']

print(access_token)
