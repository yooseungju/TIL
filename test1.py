numbers = [2,3,6,11,8]


for i in numbers:
    print(i, end=" ")

print()
    
even =[]
odd = []

num = range(11)

for i in num:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)


print(even)
print(odd)

    