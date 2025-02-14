#!/usr/bin/python3
"""
It retrieves the employee's username and their task details from the
JSONPlaceholder API.The data is then saved in a CSV file named
<employee_id>.csv.
"""
import csv
import requests
from sys import argv

def get_employee_todos_progress(employee_id):
    """returns info about the employee todos progress"""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_datas = requests.get(url + f"users?{employee_id}")
        user_data = user_datas.json()
        employee_name = user_data['username']

        """Fetch todos list for employee"""
        todos_list = requests.get(url + f"todos?userId={employee_id}")
        json_todos_list = todos_list.json()

        total_task = len(json_todos_list)
        task_done = [task for task in json_todos_list if task['completed']]
        no_task_done = len(task_done)

        """display results"""
        print(f"Employee {employee_name} is done with tasks("
              f"{no_task_done}/{task_done}):")
        
        for task in task_done:
            print(f"\t {task['title']}")

        """Export data to csv"""
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode="w", newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in json_todos_list:
                writer.writerow([employee_id, employee_name, task['completed'],
                              task['title']])

    except Exception as e:
        print(f"an error occured: (e)")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py<employee_id>")
    else:
        get_employee_todos_progress(argv[1])
