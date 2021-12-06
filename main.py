print("Welcome to Vacation Budget App")

name = input("What is your name? ")

destination = input(f"Hello, {name} Please chose your destination? Choose [1]Mexico [2]Jamaica: ")

USD = float(input("How much money in USD do you plan to spend on the trip? "))

destination_days = int(input("How many are days planning on staying? "))

if destination == "Mexico" or destination == "2":

    total_hours = destination_days * 24
    total_minutes = destination_days * 24 * 60

    print("Great, Mexico sounds like an amazing trip!")

    print(f"You will have {total_hours} hours, {total_minutes} minutes on your trip. ")

    total_cost = USD * destination_days
    cost_mxn = total_cost / 19.2
    cost_usd = cost_mxn * 19.2
    print(
        f"The total cost of the trip in MXN is {cost_mxn:.2f} and the total cost of the trip in USD is ${cost_usd:.2f} ")
    # Print a line that will just be used for formatting purposes that looks like “**********”.
    print('**********')
    print('It is a great country and you will have a lot of fun!')
    print("Thanks for using the Vacation Budget App. Enjoy your vacation! ")

if destination == "Jamaica" or destination == "2":
    total_hours = destination_days * 24
    total_minutes = destination_days * 24 * 60
    print('Great, Jamaica sounds like an amazing trip!')
    print(f"You will have {total_hours} hours, {total_minutes} minutes on your trip. ")

    total_cost = USD * destination_days
    cost_jdm = total_cost / 0.0064
    cost_usd = cost_jdm * 0.0064
    print(
        f"The total cost of the trip in Jamaica Dollar is {cost_jdm:.2f} and the total cost of the trip in USD is {cost_usd:.2f} ")
    print('**********')
    print("See you in Jamaica! ")
    print("Thanks for using the Vacation Budget App. Enjoy your vacation! ")
