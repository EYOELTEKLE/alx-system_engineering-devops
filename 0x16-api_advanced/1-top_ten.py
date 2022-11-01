#!/usr/bin/python3
"""A function that queries the Reddit API and prints the titles of
   the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed
       for a given subreddit
    """
    try:
        f = 'hot.json?limit=10'
        url = 'https://www.reddit.com/r/{}/{}'.format(subreddit, f)
        r = requests.get(url, headers={'User-agent': 'hello-student 0.1'})
        d = r.json()
        l = d.get('data').get('children')
        for i in l:
            print(i.get('data').get('title'))
    except AttributeError:
        print(None)
