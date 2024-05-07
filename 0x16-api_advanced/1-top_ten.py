#!/usr/bin/python3
""" function to queries the Reddit API and prints the titles """

import requests


def top_ten(subreddit):
    """
    param subreddit of the reddit in question:
    return: first hot titles or None
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    limit = 9
    listing = "hot"
    url = "https://www.reddit.com/r/{}/{}.json?limit={}".format(subreddit,
                                                                listing,
                                                                limit)
    header = {"User-agent": "Google Chrome Version 81.0.4044.129"}
    r = requests.get(url, headers=header)
    if r.status_code != 200:
        print("None")
        return
    else:
        response = r.json().get("data")
        for top in response.get("children"):
            print(top.get("data").get("title"))

