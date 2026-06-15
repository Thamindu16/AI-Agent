import json


def load_tasks():

    with open("data/todo.json", "r") as file:
        tasks = json.load(file)

    return tasks


def save_tasks(tasks):

    with open("data/todo.json", "w") as file:
        json.dump(tasks, file, indent=4)