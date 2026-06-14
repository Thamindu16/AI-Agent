from decision import decide
from action import execute_tool

print("AI Agent Started")
print("Type 'exit' to quit")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    tool = decide(user_input)

    response = execute_tool(tool)

    print("Agent:", response)