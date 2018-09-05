

a = 'hello'

if a.lower() == 'hello':
  print('correct')

#short version
# condition : expression
if a.lower() == 'hello': print('correct')  

#if eval
# expression if condition else expression
print(a*2) if a.lower() == 'hello' else print('No')

myList = [1, 2, 3, 4, 5]

newList = []

for n in myList:
  newList.append(n **2)
print(newList) 

# short version
#expression for variable in list

theList = [ n**2 for n in myList] 
print(theList)

