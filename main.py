Welcome_message = "Welcome to vacation planner! "

# peso = 21.736730
# jmd = 155.488

# Prompting users for their names
user_name = input("Please enter your name: ")

# Prompting users to choice a destination
answer = input("Please choice a place to travel [1]Mexico [2]Jamaica: ")

# Prompting users to choice a destination
vaca_days = input("How many days will you spend on your trip ")

spending_money = int(input("How much spending money would you like to bring? "))

# from_currency = input("From Currency: ").upper()
# to_currency = input("To Currency: ").upper()
# print(from_currency, " To ", to_currency)

# from_currency = (40 * 21.7537, "")
currency = "${:,.2f}".format(spending_money)

if answer == "1" or "Mexico":
    print(f"{Welcome_message}{user_name}Thanks for choosing Mexico.You are planning on spending {vaca_days} days in {answer} and plan to bring ${spending_money}. You can spend {spending_money * round(221.736730, 2)} MDX per day ")
elif answer == "2" or "Jamaica":
    print(f"{Welcome_message}{user_name}Thanks for choosing Jamaica! You are planning on spending {vaca_days} days in {answer} and plan to bring ${spending_money}. You can spend {spending_money*round(155.488, 2)} Jamaica Dollar per day ")
else:
    print("Please try again")

