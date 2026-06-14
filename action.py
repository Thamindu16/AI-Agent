from tools import add, subtract, multiply, divide

def execute_tool(tool_name):

    if tool_name == "add":
        return add()

    elif tool_name == "subtract":
        return subtract()

    elif tool_name == "multiply":
        return multiply()

    elif tool_name == "divide":
        return divide()

    else:
        return "Tool not found"