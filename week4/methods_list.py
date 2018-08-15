
# methods on a list

# append(n)

# reverse()

# "".join(list)
# .count()

myList = []

for n in range( 10 ):
  myList.append(n*2)
  print( myList )



myList_2 = [0,1,4,9,16,25,36]

myList_2.reverse()

print(myList_2)


myWord = 'Hello'
myWordList = list(myWord)

myWordList.reverse()

myWord = ''.join(myWordList)

print(myWord)
    