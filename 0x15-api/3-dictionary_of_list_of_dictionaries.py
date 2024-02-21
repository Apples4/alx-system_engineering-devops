#!/usr/bin/python3
""" convert data to json """

import json
import requests


if __name__ == '__main__':

    """ Fetch number of users """
    response = requests.get(f'https://jsonplaceholder.typicode.com/users')
    user_num = response.json()

    all_tasks = {}
    for user in user_num:
        user_id = user['id']
        user_name = user['name']

        """ Fetch tasks for userid """
        response = requests.get(f'https://jsonplaceholder.typicode.com'
                                f'/users/{user_id}/todos')
        todos = response.json()

        """ creating a json file """

        tasks = []
        for task in todos:
            tasks.append(
                        {"task": task["title"],
                         "completed": task["completed"],
                         "username": user_name})

        all_tasks[user_id] = tasks
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f)
