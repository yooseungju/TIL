r, c, num = map(int, input().split())
matrix = []
for _ in range(r):
    matrix.append((list(map(int, input().split()))))


hab = 0
#부분합 구하는 부분
for i in range(r):
    for j in range(1 ,c):
        matrix[i][j] += matrix[i][j-1]

for i in range(1,r):
    for j in range(0, c):
        matrix[i][j] += matrix[i-1][j]



for i in range(num):
    ax, ay, bx, by = map(int, input().split())

    ax, ay, bx, by = ax-1, ay-1, bx-1, by-1

    print(i+1 , ': ',ax, ay, bx, by)



    if ay == 0 and ax == 0:
        hab = matrix[by][bx]
    elif ax == 0:
        hab = matrix[by][bx] - matrix[ay - 1][bx]

    elif ay == 0:
        hab = matrix[by][bx] - matrix[by][ax - 1]

    else:
        hab = matrix[by][bx] - matrix[ay-1][bx] - matrix[by][ax-1] + matrix[ay-1][ax-1]


    print(hab , "dfdfa")




