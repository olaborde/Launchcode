
# List 
myList = ['a','b','c', 'd','e', 'f','g', 'h','i']



print(myList[0:6])

print(myList[-2:2])


print(myList[3:7:2])


print(myList[-2:1:-1])


print(myList[3:7:-1])

# Objects and references
# Python and Memory
#immutable 
name_1 = 'Banana'
word_1 = 'Banana'

print(name_1 == word_1)
print(name_1 is word_1)

# too different list (mulatab;e)
list_1 = ['banana', 12, 'milk']
list_2 = ['banana', 12, 'milk']

print(list_1 == list_2)
print(list_1 is list_2)
# is TRUE is they are pointing to the same object

# reassigning 

#Accumulation

a = 'Hello'

a += 'Mark'


print(a)

a = [10,20,30,40,50,50,70,80,90]

b = a

print ( b )
