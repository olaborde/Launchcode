print('******************************')
print('******************************')
print('******************************')
print('****** Filter & map **********')
print('******************************')
print('******************************')
print('******************************')

myRange = range( 100 )
# long way home
def exponent( a ):
  return a**2

newRange = []

for num in myRange:
  newRange.append(exponent(num)) 

print(newRange)

# short version with map
myRange2 = list( map(lambda a: a**2, myRange ))

print(myRange2)

#filter with condition to return only even number
myRange3 = list( filter(lambda a: a%2 == 0, myRange ))

print(myRange3)