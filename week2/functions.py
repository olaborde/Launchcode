# a function allow you to reuse a block of code anytime anywhere in your  program.abs

# def name():
#   statement

# line below invoke the function
# name(argument)  


#A parameter is the data you will be using in your block of code which will then give a specific result


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