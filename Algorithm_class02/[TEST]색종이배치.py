import sys
sys.stdin = open('input.txt')

matrix = [[0 for _ in range(100)] for _ in range(100)]


def type(cir):
    global matrix
    global mo
    I, J , N, M = map(int,input().split())
    m2 = [[I-1, J-1], [I+N-1+1, J-1], [I-1, J+N-1+1] ,[I+N-1+1, J+N-1+1]] # RU RD LU LD
    cir += (N+M) * 2

    for m in range(M): #세로
        for n in range(N): #가로
            if matrix[I+m][J+n] > 0:
                return 3
            else:
                matrix[I + m][J + n] = 1

    cnt = 0
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    
    for y in range(100):
        for x in range(100):
            if matrix[y][x] == 1:
                if y == 0 or y == 100 - 1 or x == 0 or x == 100 - 1:
                    cnt += 1
                for m in range(4):
                    if 0 <= y + di[m] < 100 and 0 <= x + dj[m] < 100:
                        if matrix[y + di[m]][x + dj[m]] == 0:
                            cnt += 1

    if cir == cnt:
        for i in m2:
            if i in mo:
                return 1
        return 4
    else:
        return 2



I, J , N, M = map(int,input().split())

mo = [[I, J], [I+N-1, J], [I, J+N-1] ,[I+N-1, J+N-1]]

for m in range(M): #세로
    for n in range(N): #가로
        matrix[I + m][J + n] = 1


cir = (N+M)*2
print(type(cir))




