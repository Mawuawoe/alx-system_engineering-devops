#!/usr/bin/python3
"""
Script that consumes an API to fetch user data and their tasks
and exports the data to a JSON file.
"""

import json
import requests

if __name__ == "__main__":
    # Fetch all users
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Dictionary to store all tasks
    all_tasks = {}

    # Loop through each user to fetch their tasks
    for user in users_data:
        user_id = user['id']
        username = user['username']

        # Fetch user tasks
        todo_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                    .format(user_id))
        tasks_response = requests.get(todo_url)
        tasks_data = tasks_response.json()

        # List of tasks for the current user
        user_tasks = [
            {"username": username,
             "task": task['title'],
             "completed": task['completed']}
            for task in tasks_data
        ]

        # Add user tasks to the all_tasks dictionary
        all_tasks[user_id] = user_tasks

    # Export all tasks to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)
