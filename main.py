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

    # Unknown command
    else:

        response = "Unknown command"

    print("Agent:", response)