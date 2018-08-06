


try:
  a = 20
  b = '5'
  print( a + c)

except NameError:
  print("Oops, something went wrong")  
else:
  print('lala')  
finally:
  print('yay')


 print("*************************")


try:
  num_1 = input("Enter the first number:")
  num_2 = input("Enter the second number:")

except ZeroDivisionError:
  print("PLease enter a number that is not sero innthe second number")  

except TypeError:
  print('Please enter numbers only')  