def add(num1, num2):
    return round(num1 + num2, 2)


def subtract(num1, num2):
    return round(num1 - num2, 2)


def multiply(num1, num2):
    return round(num1 * num2, 2)


def divide(num1, num2):

    if num2 == 0:
        return "Cannot divide by zero"

    return round(num1 / num2, 2)



from memory import load_tasks, save_tasks, load_memory, save_memory

def add_task(task):

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

    return "Task added successfully."


def view_tasks():

    tasks = load_tasks()

    if len(tasks) == 0:
        return "No tasks found."

    output = ""

    for i, task in enumerate(tasks, start=1):
        output += f"{i}. {task}\n"

    return output


def remove_task(index):

    tasks = load_tasks()

    if index < 1 or index > len(tasks):
        return "Invalid task number."

    tasks.pop(index - 1)

    save_tasks(tasks)

    return "Task removed successfully."


def remember(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)

    return "Memory saved successfully."


def recall(key):

    memory = load_memory()

    if key in memory:
        return memory[key]

    return "I don't know."