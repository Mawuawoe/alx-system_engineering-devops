#!/usr/bin/python3
"""
the first 10 hot posts listed for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Get all hot posts"""
    if after is None:
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    url += f"?limit=100&after={after}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return hot_list

    r_json = response.json()
    hot_posts_json = r_json.get("data").get("children")

    for post in hot_posts_json:
        hot_list.append(post.get("data").get("title"))

    return recurse(subreddit, hot_list, r_json.get("data").get("after"))


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    hot_posts = recurse(subreddit)
    if hot_posts:
        for title in hot_posts[:10]:  # Print only the first 10 posts
            print(title)
    else:
        print(None)
