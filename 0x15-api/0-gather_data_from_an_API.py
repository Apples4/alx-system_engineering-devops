#!/usr/bin/python3
""" script to get data from net """

import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])

    # Fetch tasks for userid
    response = requests.get(f'https://jsonplaceholder.typicode.com'
                            f'/users/{user_id}/todos')

    todos = response.json()

    total_todos = len(todos)
    done_todos = sum(1 for task in todos if task['completed'])

    # Fetch username from userid
    response = requests.get(f'https://jsonplaceholder.typicode.com'
                            f'/users/{user_id}')
    user_name = response.json()['name']  # Corrected line

    # Show progress
    print(f'Employee {user_name} is done with'
          f'tasks({done_todos}/{total_todos}):')
    for task in todos:
        if task['completed']:
            print(f"\t{task['title']}")
