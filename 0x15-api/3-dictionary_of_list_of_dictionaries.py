#!/usr/bin/python3
"""
script that exports data in JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    filename = "todo_all_employees.json"
    users = requests.get(url + "users").json()

    employee_dict = {}
    user_dict = {}
    for user in users:
        user_id = user.get("id")
        employee_dict[user_id] = []
        user_dict[user_id] = user.get("username")

    tasks = requests.get(url + "todos").json()

    for task in tasks:
        task_dict = {}
        user_id = task.get("userId")
        task_dict["username"] = user_dict.get(user_id)
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        user_dict.get(user_id).append(task_dict)

    with open(filename, "w") as json_file:
        json.dump(employee_dict, json_file)
