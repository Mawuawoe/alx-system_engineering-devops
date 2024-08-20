#!/usr/bin/python3
"""
Queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns
    the number of subscribers for a given subreddit.
    """

    # URL to get information about the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to avoid request limits imposed by Reddit
    headers = {"User-Agent": "Desmond"}

    # Sending a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    num_subs = data.get('subscribers')
    return num_subs
