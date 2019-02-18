temp = [1,2,1,2,1,1,1,1]
count = 0

if len(temp) > 2:
    for i in range(0, len(temp) - 1 ):
        print(i)
        if temp[i:i + 2] == [1, 2]:
            count += 1

print(count)