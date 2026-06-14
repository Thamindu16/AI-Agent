def decide(user_input):

    if "add" in user_input:
        return "add"

    elif "subtract" in user_input:
        return "subtract"

    elif "multiply" in user_input:
        return "multiply"

    elif "divide" in user_input:
        return "divide"

    else:
        return "unknown"