# a function allow you to reuse a block of code anytime anywhere in your  program, keep code simpler and shorter, makes it easy to read, ora=ganize code in digestible pieces, prevent repeat long block of code

# def name():
#   statement

# line below invoke the function
# name(argument)  


#A parameter is the data you will be using in your block of code which will then give a specific result

# refactor repeating code with functions, DO NOT reapt you code
# a function is just fuctionality


def square(n):
  the_square = n * n
  return the_square

print(square(10))  
print(square(3))  
print(square(43)) 

print("*************Addition*************")


def add(a, b):
  addition = a + b
  return addition

print(add(10,4))

print("*************Calculation*************")


def calc(n):
  the_calc = (n**2)+(n*3)-(n/2)
  return the_calc

print( calc(74))  


def say_appointment(name, app_time):
  greet = "Hello "+ name + ", my name is Osse, our appointment is at "+ str(app_time)+ " o'clock"

  return greet


print(say_appointment("joe", 7))


# global vs local scope


item = "I love "


def test():
  print(item)

  item = 'I am the boss'
  print(item)

test()


a = 10
b = 3

print( a % b)


def password_checker( password ):
  stored_pass = "lougarouvole"

  if password == stored_pass:
    print("correct")
  else:
    print("wrong") 


guessed_password = input("Guess the password:")     
password_checker(guessed_password)

# function with multiple retun values
def get_boundaries(target, margin):
      low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit

low, high = get_boundaries(100, 20)

print('Low limit: '+ str(low) +', high limit: '+str(high))


# scope

time = "3pm"
mood = "good"

def report():
  print("The current time is " + time)
  print("The mood is " + mood)

print("End of report")

report()