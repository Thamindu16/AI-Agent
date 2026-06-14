from tools import add, subtract, multiply, divide

tools = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}


def execute_tool(tool_name, num1, num2):

    if tool_name in tools:
        return tools[tool_name](num1, num2)

    return "Tool not found"