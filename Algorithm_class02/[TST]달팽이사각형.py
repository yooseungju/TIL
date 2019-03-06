import sys
sys.stdin = open('input.txt')

N =int(input())
M = [[0 for _ in range(N)] for _ in range(N)]
value = 1
Di = [0, 1, 0, -1]
Dj = [1, 0 ,-1, 0]

d = 0
flag = 0
i = 0
j = 0

while N > 0:
    n = 0
    if not flag:
        M[0][0] += value
        value += 1
        flag = 1
        n += 1

    if flag:
        while n < N:
            i += Di[d]
            j += Dj[d]
            M[i][j] = value
            value += 1
            n += 1

    if d == 0:
        N -= 1
    if d == 2:
        N -= 1
    if d == 3:
        d =-1

    d += 1

for i in range(len(M)):
    for j in range(len(M)):
        print(M[i][j], end = ' ')
    print()