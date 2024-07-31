#!/usr/bin/python3
"""
Script that consumes an API to fetch user data and their tasks.
"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Fetch user data
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('username')

    # Fetch user tasks
    todo_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    tasks_response = requests.get(todo_url)
    tasks_data = tasks_response.json()
    num_tasks = len(tasks_data)
    done_tasks = [task['title'] for task in tasks_data if task['completed']]
    num_done_tasks = len(done_tasks)

    """# Export tasks to CSV
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID",
                         "USERNAME",
                         "TASK_COMPLETED_STATUS",
                         "TASK_TITLE"])
        for task in tasks_data:
            writer.writerow([user_id,
                             employee_name,
                             task['completed'],
                             task['title']])"""
    # Export tasks to CSV
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks_data:
            writer.writerow([user_id,
                             employee_name,
                             task['completed'],
                             task['title']])
