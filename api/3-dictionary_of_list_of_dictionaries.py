#!/usr/bin/python3
"""It retrieves the usernames and their task details.
The data is then saved in a JSON file named `todo_all_employees.json`.
"""
import json
import requests


def get_employee_tasks(employee_id):
    """
    Fetches tasks for a specific employee from the API.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    try:
        # Fetch employee details
        user_info = requests.get(user_url).json()
        employee_username = user_info.get("username")

        # Fetch employee's TODO list
        todos_info = requests.get(todos_url).json()

        # Prepare tasks in the required format
        tasks = [
            {
                "username": employee_username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in todos_info
        ]
        return tasks

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for employee {employee_id}: {e}")
        return []


def get_all_employee_ids():
    """
    Fetches all employee IDs available in the API.
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    try:
        users_info = requests.get(base_url).json()
        return [user.get("id") for user in users_info]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching employee IDs: {e}")
        return []


if __name__ == '__main__':
    # Fetch all employee IDs
    all_employee_ids = get_all_employee_ids()

    # Collect tasks for all employees
    all_employees_tasks = {}
    for emp_id in all_employee_ids:
        all_employees_tasks[str(emp_id)] = get_employee_tasks(emp_id)

    # Write data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_employees_tasks, json_file, indent=4)

    print("Data exported to todo_all_employees.json")
