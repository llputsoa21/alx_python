""" extend Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv """


import json
import requests
import sys


def get_user_data(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(url, user_id)
    response = requests.get(user_url)
    return response.json()


def get_user_tasks(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    todos_url = "{}todos?userId={}".format(url, user_id)
    response = requests.get(todos_url)
    return response.json()


def export_all_to_json():
    all_tasks = {}
    for user_id in range(1, 11):  # Assuming user IDs range from 1 to 10
        user_data = get_user_data(user_id)
        user_tasks = get_user_tasks(user_id)

        l_task = []
        for task in user_tasks:
            dict_task = {
                "username": user_data.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            l_task.append(dict_task)

        all_tasks[str(user_id)] = l_task

    filename = "todo_all_employees.json"
    with open(filename, "w") as json_file:
        json.dump(all_tasks, json_file, indent=2)


if __name__ == "__main__":
    export_all_to_json()