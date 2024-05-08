#!/usr/bin/python3
""" function to queries the Reddit API and prints the titles """

import requests


def recurse(subreddit, hot_list=[]):
    """
    param subreddit: subreddit we are interested in
    param hot_list: looking at the hot titles
    return: None or list of hot titles
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
    global after
    limit = 100
    listing = "hot"
    url = "https://www.reddit.com/r/{}/{}.json?limit={}".format(subreddit,
                                                                listing,
                                                                limit)
    header = {"User-agent": "Google Chrome Version 81.0.4044.129"}
    r = requests.get(url, headers=header, allow_redirects=False)

    if r.status_code == 200:
        info = r.json().get("data").get("after")
        if info is not None:
            after = info
            recurse(subreddit, hot_list)
        titles = r.json().get("data").get("children")
        for i in titles:
            hot_list.append(i.get("data").get("title"))
        return hot_list
    else:
        print("None")
