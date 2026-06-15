from tools import add, subtract, multiply, divide, add_task, view_tasks

tools = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "add_task": add_task,
    "view_tasks": view_tasks
}


def execute_tool(tool_name, *args):

    if tool_name in tools:
        return tools[tool_name](*args)

    return "Tool not found"