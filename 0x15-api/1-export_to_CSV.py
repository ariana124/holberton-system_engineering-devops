#!/usr/bin/python3
"""
script that exports data in CSV format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    employee = requests.get(url + "users/" + employee_id).json()
    tasks = requests.get(url + "todos?userId=" + employee_id).json()

    name = employee.get("name")
    filename = employee_id + ".csv"

    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow((task.get("userId"),
                             name,
                             task.get("completed"),
                             task.get("title")))
