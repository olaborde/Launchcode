

try:
  a = 20
  b = '5'
  print( a + b)

except NameError:
  print("Oops, something went wrong")  
else:
  print('lala')  
finally:
  print('yay')