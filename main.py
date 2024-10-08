import pandas as pd
from api import request

def print_header():
    print("##########################################################################")
    print("################## Reddit Sports Highlight CLI Tool ######################")
    print("##########################################################################")
    print("Supported subreddits: soccer, nfl")

def main():
    print_header()
    user_input = input("Enter a subreddit you would like to see highlight links for: ")
    sub_data = request(user_input)
    df = pd.DataFrame()

    titles = []
    links = []

    for post in sub_data.new(limit=20):
        if user_input == "soccer":
            if post.link_flair_text == 'Media':
                titles.append(post.title)
                links.append(post.url_overridden_by_dest)
        if user_input == "nfl":
            if post.link_flair_text == 'Highlight':
                titles.append(post.title)
                links.append(post.url_overridden_by_dest)

    #print(vars(post))
    df['Title'] = titles
    df['Link'] = links

    print(df.to_string())

main()
