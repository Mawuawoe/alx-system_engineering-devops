#!/usr/bin/python3
"""
script that consumes an api
"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = (sys.argv[1])

    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))

    #print(response)
    # print(response.json())
    employeeName = response.json().get('name')
    #print("Employee {} is done with tasks".format(employeeName))

    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id))
    numTasks = len(tasks.json())
    #print(numTasks)
    numdoneTask = 0
    doneTask = []
    for task in tasks.json():
        if task.get('completed'):
            doneTask.append(task.get('title'))
            numdoneTask += 1

    print("Employee {} is done with tasks({}/{}):".format(employeeName, numdoneTask, numTasks))
    for task in doneTask:
        print(f"\t{task}")
