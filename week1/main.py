# Donuts assignmnts

sales_tax = 5 / 100
print(""" Welcome to the Loop Hole!
Today's Manager's Special is:
Crunch Jelly: A traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch Oops! All Berries """)

number_of_donuts = int(input("How many would you like?:"))



donut_price = float(input("How much would you like to pay per donut (suggested price is $4.35 each)?"))

total_price = float(sales_tax + ( number_of_donuts * donut_price))


print("Ok, let me prepare that for you....")
print("After tax, your total is:", total_price)