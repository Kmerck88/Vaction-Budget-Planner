# Welcome Message

Welcome_message = "Welcome to vacation planner! "

print(Welcome_message)

# Prompting users for their names
user_name = input("Please enter your name: ")

# Prompting users to choice a destination 
answer = input("Please choice a place to travel (1)Mexico (2)Jamaica: ")

# Prompting users to choice a destination 
vaca_days = int(input(f"How many days they will spend on the trip "))
# Prompting users for spendong money 
spending_money = int(input("How much spending money would like to bring?  "))

vaca_math = spending_money / vaca_days

#implemeted currency formatting for the currency solution 
#match 


currency = "${:,.2f}".format(vaca_math)



if answer == "Mexico":
    print(f"{Welcome_message}{user_name}Thanks for choosing Mexico.You are planning on spending {vaca_days} days in {answer} and plan to bring ${spending_money}. You can spend {currency} per day  ")
elif answer == "Jamaica":
    print(f"{Welcome_message}{user_name}Thanks for choosing Jamaica! You are planning on spending {vaca_days} days in {answer} and plan to bring ${spending_money}. You can spend {currency} per day  ")
elif answer == "Q":
    exit 
