from decision import decide
from action import execute_tool

user_input = input("You: ")

tool = decide(user_input)

response = execute_tool(tool)

print("Agent:", response)