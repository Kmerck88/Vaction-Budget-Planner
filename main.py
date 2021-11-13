# Welcome Message

Welcome_message = "Welcome to vacation planner! "

print(Welcome_message)

# Prompting users for their names
user_name = input("Please enter your name: ")


# Prompting users to choice a destination 
answer = input("Do you want to Travel: A) Jamica. B)Mexico. [A/B]?: ")


if answer == "A":
    print(f"{Welcome_message}{user_name}Thanks for choicing Mexico.")
elif answer == "B":
    print(f"{Welcome_message}{user_name}Thanks for choicing Jamica")
elif answer == "Q":
    exit
