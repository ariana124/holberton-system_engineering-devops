#!/usr/bin/python3
"""
script that uses an API to return information about an employee's TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    employee = requests.get(url + "users/" + employee_id).json()
    tasks = requests.get(url + "todos?userId=" + employee_id).json()

    tasks_completed = []
    for task in tasks:
        if task.get("completed") is True:
            tasks_completed.append(task)

    completed_tasks = len(tasks_completed)
    total_tasks = len(tasks)
    name = employee.get("name")

    print("Employee {} is done with tasks({}/{}):".format(name, completed_tasks,
                                                          total_tasks))
    for task in tasks_completed:
        print("\t {}".format(task.get("title")))
