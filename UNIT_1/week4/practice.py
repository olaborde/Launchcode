from random import shuffle

sentence = 'The world is too big'

list_1 = ['Hello', 'my', 'name', 'is', 'Osse']
# print(sentence[0:2:5])

shuffle(list_1)

print(list_1)

print(ord('e'))
print(ord('E'))
print('*********************************')
password = 'Banana'

newPassword = ''
#make every character slide 3 Unicode numbers

# for n in password:
#   uni = ord( n )
#   print(n, ":", uni)
#   newUni = uni + 3
#   print(chr(newUni), ":", newUni)
#   print('-------')
#   newPassword = newPassword + chr(newUni)

# print(newPassword)  



i= 0
while i < len(password):
  n = password[i]

  if i % 2 == 0:
    uni = ord( n )
    newUni = uni + 3
    newPassword = newPassword + chr( newUni )
  else:
    newPassword = password + n  
  i += 1

print(newPassword)  

# list split and join

stri = 'Hello Bob, How are you?'
print(stri)

print( stri.split(" "))

myList = stri.split(' ')
print( myList)
print("-".join(myList))

shuffle( myList)

print( myList )

# list


stro = 'Hello Bob, How are you?'

print(list(stro))

print("*************")

for n in stro:
  print( n )