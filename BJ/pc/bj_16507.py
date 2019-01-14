r, c, num = map(int, input().split())
matrix = []
for _ in range(5):
    matrix.append((list(map(int, input().split()))))


print(matrix)

hab = '0'

for i in range(r):
    for j in range(0 , c):
        if i == 0:
            if j != 0:
                matrix[i][j] += matrix[i][j-1]


        elif i > 0 and j > 0:
            matrix[i][j] += matrix[i-1][j-1]

        else:
            matrix[i][j] += matrix[i-1][j]


    









print(matrix)



