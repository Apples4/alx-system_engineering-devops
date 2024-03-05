#!/usr/bin/python3
'''
script to returns a list containing the titles of all
hot articles for a given subreddit
'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
    params - subreddit from reddit
             hot_list - empty list
    return - a list containing the titles of all hot articles
    '''
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    listing = 'hot'
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = f'https://www.reddit.com/r/{subreddit}/{listing}.json'
    response = requests.get(url,
                            params={'after': after},
                            headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        response = response.json()
        posts = response['data']['after']
        if posts is not None:
            after = posts
            recurse(subreddit, hot_list)
        titles = response['data']['children']
        for title in titles:
            hot_list.append(response['data']['titles'])
        return hot_list
    else:
        return None
