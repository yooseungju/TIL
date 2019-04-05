import sys
sys.stdin = open('input.txt')

def BFS():
    global MIN
    dj = [-1,1,0,0]
    di = [0,0,-1,1]
    rec[sx][sy][0] = 1
    Q = [(sx, sy, 0)]
    while Q:
        x, y, z = Q.pop(0)
        for m in range(4):
            nx = x + di[m]
            ny = y + dj[m]
            if 1 <= nx < R-1 and 1 <= ny < C-1:
                if arr[nx][ny] == 0 and not rec[nx][ny][z]:
                    rec[nx][ny][z] = rec[x][y][z] + 1
                    Q.append((nx,ny,z))

                elif arr[nx][ny] == 2:
                    if z < 3 and not rec[nx][ny][z+1]:
                        rec[nx][ny][z+1] = rec[x][y][z] + 1
                        Q.append((nx, ny, z+1))

                if arr[nx][ny] == 4:
                    MIN = rec[x][y][z]
                    return



# 세로 가로
R, C = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
sx=0
sy=0
ex=0
ey=0

for i in range(1,R):
    for j in range(1,C):
        if arr[i][j] == 3:
            sx = i
            sy = j
        elif arr[i][j] == 4:
            ex = i
            ey = j


rec = [[[0]*4 for _ in range(C)] for _ in range(R)]
MIN = 0
BFS()

if not MIN:
    print(-1)
else:
    print(MIN)

