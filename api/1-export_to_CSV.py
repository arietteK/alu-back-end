#!/usr/bin/python3
"""
It retrieves the employee's username and their task details from the
JSONPlaceholder API.The data is then saved in a CSV file.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    # Base URL for the API
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    # Fetch employee ID from command line argument
    EMP_ID = sys.argv[1]

    # Fetch employee details
    employee_url = f'{BASE_URL}/users/{EMP_ID}'
    todos_url = f'{BASE_URL}/users/{EMP_ID}/todos'

    try:
        # Fetch employee data
        employee = requests.get(employee_url).json()
        EMPLOYEE_NAME = employee.get("username")

        # Fetch employee's TODO list
        todos = requests.get(todos_url).json()

        # Write data to CSV file
        with open(f'{EMP_ID}.csv', mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for todo in todos:
                writer.writerow([
                    EMP_ID,
                    EMPLOYEE_NAME,
                    str(todo.get("completed")),
                    todo.get("title")
                ])

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
