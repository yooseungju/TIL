import sys
sys.stdin = open('input.txt')



dy = (-1,1,0,0)
dx = (0,0,-1,1)

def BFS(empty):
    global MIN
    visited = [[0]*N for _ in range(N)]
    Q = []

    for t in tmp:
        x, y = virus[t]
        visited[x][y] = 1
        Q.append((x,y,0))


    while Q:
        x, y, c = Q.pop(0)
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if M[nx][ny] == 0:
                    empty -= 1

                    if empty == 0:
                        if c < MIN:
                            MIN = c +1
                        return

                    visited[nx][ny] = 1
                    Q.append((nx,ny,c+1))

                elif M[nx][ny] == 2:
                    visited[nx][ny] = 1
                    Q.append((nx,ny,c+1))

def com(n,s):
    if n == P:
        BFS(empty)
        return

    for i in range(s,length):
        tmp[n] = i
        com(n+1, i+1)
        tmp[n] = 0


N , P = map(int, input().split())

M = [list(map(int, input().split())) for _ in range(N)]

virus = []

empty = 0
MIN = 0xfffffff
for i in range(N):
    for j in range(N):
        if M[i][j] == 2:
            virus.append((i,j))
        elif M[i][j] == 0:
            empty += 1

length = len(virus)
tmp = [0]*P

if empty == 0:
    print(0)
else:
    com(0, 0)

    if MIN == 0xfffffff:
        print(-1)
    else:
        print(MIN)