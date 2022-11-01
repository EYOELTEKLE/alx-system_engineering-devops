#!/usr/bin/python3
"""This file contains a function that queries the Reddit API
   and returns a list containing the titles of all hot articles for
   a given subreddit. If no results are found for the given subreddit,
   the functio returns None.
"""

import requests


def recurse(subreddit, hot_list=[], page=""):
    """main recursive function that handles initial page
    """
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        r = requests.get(url, headers={'User-Agent': 'hello-student 0.4'},
                         params={'limit': 100})
        d = r.json()
        hot_list.extend(d['data']['children'])
        page = d['data']['after']
        if d['data']['after'] is None:
            return
    except KeyError:
        return None
    recursive(subreddit, hot_list, page)
    return hot_list


def recursive(subreddit, hot_list=[], page=""):
    """handles the other entries"""
    if page is None:
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'hello-student 0.4'},
                     params={'after': page, 'limit': 100})
    d = r.json()
    hot_list.extend(d['data']['children'])
    return recursive(subreddit, hot_list, d['data']['after'])
