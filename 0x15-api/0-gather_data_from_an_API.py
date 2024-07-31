#!/usr/bin/python3
"""
Script that consumes an API to fetch user data and their tasks.
"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Fetch user data
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch user tasks
    todo_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    tasks_response = requests.get(todo_url)
    tasks_data = tasks_response.json()
    num_tasks = len(tasks_data)
    done_tasks = [task['title'] for task in tasks_data if task['completed']]
    num_done_tasks = len(done_tasks)

    # Print results
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_done_tasks, num_tasks))
    for task in done_tasks:
        print(f"\t{task}")
