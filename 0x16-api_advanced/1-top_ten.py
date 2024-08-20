#!/usr/bin/python3
"""
the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "subreddit-post-fetcher/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts[:10]:  # Get only the first 10 posts
                print(post["data"]["title"])
        else:
            print(None)
    except requests.RequestException:
        print(None)
