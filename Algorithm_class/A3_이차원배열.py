arr = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]

for row in range(len(arr)):
    for col in range(len(arr[row])):
        print(arr[row][col], end = " ")
    print()
print()

for col in range(len(arr[0])):
    for row in range(len(arr)):
        print(arr[row][col], end = " ")
    print()
print()

