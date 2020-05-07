#!/usr/bin/python3
"""
Query that uses the Reddit API and prints the titles of the first
top 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/" + subreddit
    headers = {"User-Agent": "Mozilla 5.0"}

    response = requests.get(url + "/hot.json?limit=10", headers=headers)

    # If the page was found, then it will return the top ten hot posts.
    if (response.status_code == 200):
        data = response.json().get("data")
        posts = data.get("children")
        for key in posts:
            print(key.get("data").get("title"))
    else:
        print("None")
