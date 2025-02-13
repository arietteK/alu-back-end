#!/usr/bin/python3

import json
import requests

def get_employee_tasks():
    """returns info about the employee"""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_response = requests.get(url + f"users")
        user_data = user_response.json()
        
        """puting all the employee data in a dictinary"""
        all_employee_task = {}
        
        for user in user_data:
            employee_id = user['id']
            employee_name = user['username']

            """ getting the todo list"""
            todo_response = requests.get(url + f"todos?userId={employee_id}")
            todo_list = todo_response.json()

        """Json data"""
        tasks = [
            {
                "username": employee_name,
                "tasks": task["title"],
                "completed": task["completed"]
            }
            for task in todo_list
        ]
        all_employee_task[str(employee_id)] = tasks

        json_filename = "todo_all_employees.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(all_employee_task, json_file, indent= 4)

    except Exception as e:
        print(f"an error occured: (e)")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: Script<employee_id>")
    else:
        get_employee_todos_progress(argv[1])
