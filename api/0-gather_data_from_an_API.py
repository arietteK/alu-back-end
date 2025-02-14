#!/usr/bin/python3
"""
Using a REST API, it fetches the employee's name and tasks from the
JSONPlaceholder API, keeps a record of the work done, and prints the progress.
"""

import requests
import sys


if __name__ == "__main__":
    # Base URL for the API
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    # Fetch employee details
    employee_id = sys.argv[1]
    employee_url = f'{BASE_URL}/users/{employee_id}'
    todos_url = f'{BASE_URL}/users/{employee_id}/todos'

    try:
        # Fetch employee data
        employee = requests.get(employee_url).json()
        EMPLOYEE_NAME = employee.get("name")

        # Fetch employee's TODO list
        todos = requests.get(todos_url).json()

        # Calculate completed tasks
        completed_tasks = [todo for todo in todos if todo.get("completed")]
        total_tasks = len(todos)
        completed_len = len(completed_tasks)

        # Print the required output
        print(
            f"Employee {EMPLOYEE_NAME} is done with tasks"
            f"({completed_len}/{total_tasks}):"
        )
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
