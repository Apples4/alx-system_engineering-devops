#!/usr/bin/python3
""" script that access API """
""" importing libraries"""
import requests


def number_of_subscribers(subreddit):
    """ 
    function that prints number of subscribers
    param: subreddit url address
    returns - number of subscriber to the subreddit or 0
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    header = {"User-agent": "Google Chrome Version 81.0.4044.129"}
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers=header)
    response = r.json()

    try:
        return response["data"]["subscribers"]
    except Exception:
        return 0
