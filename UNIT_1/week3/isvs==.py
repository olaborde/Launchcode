# is vs ==
# == check for equality, 
# is compare identity,and same content


a = [0,1,2,3,4,5,6,7,8,9]

b = a

print(a==b)

print(a is b)


a[0] = 'Mundo'

print(b)

c = list(a)

print(c)

print(a==b)
print(a==c)


print(a is b)
print(a is c)