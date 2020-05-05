#!/usr/bin/python3
"""
script that exports data in JSON format
"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    employee = requests.get(url + "users/" + employee_id).json()
    tasks = requests.get(url + "todos?userId=" + employee_id).json()

    username = employee.get("username")
    filename = employee_id + ".json"

    employee_tasks = []
    for task in tasks:
        employee_tasks.append({"task": task.get("title"),
                               "completed": task.get("completed"),
                               "username": username})

    employee_dict = {argv[1]: employee_tasks}
    with open(filename, "w") as json_file:
        json.dump(employee_dict, json_file)
