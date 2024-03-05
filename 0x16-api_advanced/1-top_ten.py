#!/usr/bin/python3
''' 
script that prints the titles of the first 10 hot
posts listed for a given subreddit
'''

import requests


def top_ten(subreddit):
    '''
    params - subreddit from reddit
    Returns -  first 10 hot posts listed
    '''
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    listing = 'hot'
    count = 10
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={count}'
    response = requests.get(url, headers=headers)
    response = response.json()

    try:
        for post in response['data']['children']:
            x = post['data']['title']
            if '[META]' not in x:
                print(x)
    except requests.RequestException:
        return None
