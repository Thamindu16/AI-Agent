import json


def load_tasks():

    with open("data/todo.json", "r") as file:
        tasks = json.load(file)

    return tasks


def load_memory():

    with open("data/memory.json", "r") as file:
        memory = json.load(file)

    return memory


def save_tasks(tasks):

    with open("data/todo.json", "w") as file:
        json.dump(tasks, file, indent=4)


def save_memory(memory):

    with open("data/memory.json", "w") as file:
        json.dump(memory, file, indent=4)