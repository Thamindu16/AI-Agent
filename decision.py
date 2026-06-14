commands = {
    "add": "add",
    "plus": "add",

    "subtract": "subtract",
    "minus": "subtract",

    "multiply": "multiply",
    "times": "multiply",

    "divide": "divide"
}


def decide(user_input):

    user_input = user_input.lower()

    if user_input in commands:
        return commands[user_input]

    return "unknown"