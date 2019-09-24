import sys
sys.stdin = open('input.txt')

dy = (-1,1,0,0)
dx = (0,0,-1,1)

def BFS():
    global cnt, MIN
    Q = [(0,0)]
    M[0][0] = 1

    while Q:
        x,y= Q.pop(0)

        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            if 0<= nx < R+1 and 0<= ny < C+1 and (not M[nx][ny] or M[nx][ny] >= M[x][y]+1) and MIN > M[x][y]:
                if nx == cx and ny == cy:
                    M[nx][ny] = M[x][y] + 1
                    MIN = M[nx][ny]
                    cnt += 1
                else:
                    M[nx][ny] = M[x][y] + 1
                    Q.append((nx,ny))


cnt = 0
R, C = map(int, input().split())
M = [[0]*(C+1) for _ in range(R+1)]
tmp = [[0]*(C+1) for _ in range(R+1)]

for i in range()

cx, cy = map(int, input().split())
MIN = 0xfffffff
if cx > R or cy > C:
    print('fail')
else:
    BFS()
    print(cnt)
    print(MIN-1)
