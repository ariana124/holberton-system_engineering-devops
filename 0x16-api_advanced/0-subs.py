#!/usr/bin/python3
"""
Query that uses the Reddit API to get the number of subscribers for a
given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/" + subreddit
    headers = {"User-Agent": "Mozilla 5.0"}

    response = requests.get(url + "/about.json", headers=headers)

    # If the page was found, then it will return the subscriber count.
    if (response.status_code == 200):
        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    else:
        return 0
