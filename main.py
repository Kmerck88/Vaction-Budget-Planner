# Welcome Message

Welcome_message = "Welcome to vacation planner! "

print(Welcome_message)

# Prompting users for their names
user_name = input("Please enter your name: ")


# Prompting users to choice a destination 
answer = input("Do you want to Travel: Jamica) Please type Jamica : ")


# Prompting users to choice a destination 
vaca_days = (int(input(f"How many days they will spend on the trip ")))
# Prompting users for spendong money 
spending_money = int(input("how much “spending money” would like to bring?  "))
vaca_math = spending_money / vaca_days



if answer == "Jamica":
    print(f"{Welcome_message}{user_name}Thanks for choicing Jamica You are planning on spending {vaca_days} in {answer} and plan to bring ${spending_money}. You can spend ${vaca_math}0 per day  ")
# elif answer == "Mexico":
#     print(f"{Welcome_message}{user_name}Thanks for choicing Jamica")
elif answer == "Q":
    exit 
