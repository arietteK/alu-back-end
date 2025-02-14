#!/usr/bin/python3
"""
It retrieves the employee's username and their task details.
The data is then saved in a JSON file.
"""
import json
import requests
import sys


if __name__ == "__main__":
    # Base URL for the API
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    # Fetch employee ID from command line argument
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        # Fetch employee details
        employee_url = f'{BASE_URL}/users/{employee_id}'
        todos_url = f'{BASE_URL}/users/{employee_id}/todos'

        employee = requests.get(employee_url).json()
        employee_name = employee.get("username")

        # Fetch employee's TODO list
        todos = requests.get(todos_url).json()

        # Prepare data for JSON export
        tasks = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee_name
            }
            for todo in todos
        ]

        output_data = {employee_id: tasks}

        # Write data to JSON file
        file_name = f"{employee_id}.json"
        with open(file_name, 'w') as file:
            json.dump(output_data, file, indent=4)

        print(f"Tasks for employee {employee_id} exported to {file_name}.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
