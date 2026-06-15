commands = {
    "add": "add",
    "plus": "add",

    "subtract": "subtract",
    "minus": "subtract",

    "multiply": "multiply",
    "times": "multiply",

    "divide": "divide",
    "add_task": "add_task",
    "view_tasks": "view_tasks",
    "remove_task": "remove_task",
    "remember": "remember",
    "recall": "recall"
}


def decide(user_input):

    user_input = user_input.lower()

    if user_input in commands:
        return commands[user_input]

    return "unknown"