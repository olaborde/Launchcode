for n in range(100):
    if n % 2 == 0:
        continue
print(n)  



print("************************Leap year with break and continue*************")

for y in range(1000, 2030):
    if y % 400 == 0:
        print(y)
        break
    elif y % 100 == 0:
        continue
    elif y % 4 == 0:
        print(y)
        break    