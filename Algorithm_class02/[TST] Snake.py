import sys
sys.stdin = open('input.txt')

SIZE = 10001
N = int(input())
M = [[0 for _ in range(N)] for  _ in range(N)]
K = int(input())

for _ in range(K):
    r,c  = map(int, input().split())
    M[r-1][c-1] = 1

L = int(input())
second = [0]*SIZE

for _ in range(L):
    C =input().split()
    second[int(C[0])] = C[1]

# 우 하 좌 상
di = [0,1,0,-1]
dj = [1,0,-1,0]

i = 0
j = 0
d = 0

def isWall(x, y):
    if x < 0 or x > N-1 or y<0 or y>N-1:
        return True
    return False

for s in range(1, SIZE):
    if second[s] == 'L':
        if d == 0:
            d = 3
        else:
            d -= 1
    elif second[s]  == 'D':
        if d == 3:
            d = 0
        else:
            d += 1
    else:
        if isWall(i+di[d],j+dj[d]) or M[i+di[d]][j+dj[d]] == 2:
            print(s)
            break

        elif M[i+di[d]][j+dj[d]] == 0:
            i += di[d]
            j += dj[d]
            M[i][j] = 2

        elif M[i+di[d]][j+dj[d]] == 1:
            i += di[d]
            j += dj[d]
            M[i][j] = 2
for i in range(N):
    for j in range(N):
        print(M[i][j], end=' ')
    print()