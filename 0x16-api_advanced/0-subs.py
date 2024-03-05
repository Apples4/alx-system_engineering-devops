#!/usr/bin/python3
''' script to returns the number of subscribers in subreddit '''

import requests


def number_of_subscribers(subreddit):
    '''
    params - subreddit from reddit
    Returns - subscribers in subredit or 0
    '''
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    response = response.json()
    try:
        return response['data']['subscribers']
    except Exception:
        return 0
