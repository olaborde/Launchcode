


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


  def division_calc():  
  try:
    num_1 = input('enter first number:')
    num_2 = input( 'enter second number:' )
    
    print( int(num_1) / int(num_2) )

  except ZeroDivisionError:
    print( "Please put a number that is not ZERO in the second number" )
    division_calc()

  except ValueError:
    print( "Please put numbers only" )
    division_calc()

  except:
    print('Something went wrong.')
    division_calc()

division_calc()