#!/usr/bin/python3
""" convert data to json """

import json
import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])

    """ Fetch tasks for userid """
    response = requests.get(f'https://jsonplaceholder.typicode.com'
                            f'/users/{user_id}/todos')
    todos = response.json()

    total_todos = len(todos)
    done_todos = sum(1 for task in todos if task['completed'])

    """ Fetch username from userid """
    response = requests.get(f'https://jsonplaceholder.typicode.com'
                            f'/users/{user_id}')
    user_name = response.json()['name']

    """ creating a json file """

    tasks = []
    for task in todos:
        tasks.append(
                    {"task": task["title"],
                     "completed": task["completed"],
                     "username": user_name})

    with open('USER_ID.json', 'w') as f:
        json.dump({user_id: tasks}, f)
