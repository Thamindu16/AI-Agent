from decision import decide
from action import execute_tool

print("AI Agent Started")
print("Type 'exit' to quit")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    parts = user_input.split()

    if len(parts) == 0:
        continue

    command = parts[0]

    tool = decide(command)

    # Calculator tools
    if tool in ["add", "subtract", "multiply", "divide"]:

        if len(parts) != 3:
            print("Invalid format")
            continue

        num1 = float(parts[1])
        num2 = float(parts[2])

        response = execute_tool(tool, num1, num2)

    # Add task
    elif tool == "add_task":

        if len(parts) < 2:
            print("Please enter a task.")
            continue

        task = " ".join(parts[1:])

        response = execute_tool(tool, task)

    # View tasks
    elif tool == "view_tasks":

        response = execute_tool(tool)

    # Remove task
    elif tool == "remove_task":

        if len(parts) != 2:
            print("Invalid Format")
            continue

        task_number = int(parts[1])

        response = execute_tool(tool, task_number)

    # Remember information
    elif tool == "remember":

        if len(parts) < 3:
            print("Invalid format")
            continue

        key = parts[1]
        value = " ".join(parts[2:])

        response = execute_tool(tool, key, value)

    # Recall information
    elif tool == "recall":
        # print("Tool =", tool)

        if len(parts) != 2:
            print("Invalid format")
            continue

        key = parts[1]

        response = execute_tool(tool, key)

    # Unknown command
    else:

        response = "Unknown command"

    print("Agent:", response)