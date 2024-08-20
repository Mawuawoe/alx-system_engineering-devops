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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Custom User-Agent to avoid request limits imposed by Reddit
    headers = {"User-Agent": "EclectrochemApp/1.0"}

    try:
        # Sending a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:

            # Parse the JSON response into a Python dictionary
            data = response.json()

            # Return the number of subscribers
            # (if present), otherwise return 0
            return data['data'].get('subscribers', 0)
        else:
            # If the status code is not 200, return 0
            return 0
    except requests.RequestException:
        return 0
