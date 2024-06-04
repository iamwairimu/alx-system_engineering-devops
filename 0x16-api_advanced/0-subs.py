#!/usr/bin/python3
"""
Function that query subscribers on a given Reddit subreddit.
"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def number_of_subscribers(subreddit):
    """
    Parameters:
    - subreddit (str): The name of the subreddit to query.

    Returns:
    - int: The total number of subscribers on the subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
