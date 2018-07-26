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


# Write a general version of the program which asks for the day number that your vacation starts on and the length of your holiday, and then tells you the number of the day of the week you will return on.


# It is possible to name the days 0 through 6, where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day 3 (a Wednesday) and you return home after 10 nights, you arrive home on day 6 (a Saturday).


print(" Please enter a day number from 0 through 6, where ) is Sunday the first day of the week")

day_number = int(input(" what day number your vacation starts"))

holiday_length = int(input(" How long you will be on vaction for?"))

return_day = abs((day_number + holiday_length)% 7 )


if return_day == 0:
    return_day = 'Sunday'
elif return_day == 1:
  return_day = 'Monday'
elif return_day == 2:
  return_day = 'Tuesday'
elif return_day == 3:
  return_day = 'Wednesday'
elif return_day == 4:
  return_day = 'Thursday'
elif return_day == 5:
  return_day = 'Friday' 
elif return_day == 6:
  return_day = 'Saturday'         


print("You will return on the", return_day)