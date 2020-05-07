#!/usr/bin/python3
"""
Query that uses the Reddit API and returns a list containing all the titles of
all hot articles of a given subreddit or returns None if there are no results
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/" + subreddit
    headers = {"User-Agent": "Mozilla 5.0"}
    new_url = url + "/hot.json?limit=100&after=" + str(after)

    response = requests.get(new_url, headers=headers)

    if (response.status_code == 200):
        data = response.json()
        posts = data.get("data").get("children")
        after = data.get("data").get("after")

        for post in posts:
            hot_list.append(post.get("data").get("title"))

        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list
    else:
        return None
