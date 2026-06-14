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

    if len(parts) != 3:
        print("Invalid format")
        continue

    command = parts[0]
    num1 = float(parts[1])
    num2 = float(parts[2])

    tool = decide(command)

    response = execute_tool(tool, num1, num2)

    print("Agent:", response)