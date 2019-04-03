import sys
sys.stdin = open("input.txt")

SIZE = 3



def BFS(i,j, pre, M,cnt):
    global S, MIN

    dj = [-1,1,0,0]
    di = [0,0,-1,1]

    Q = [[i,j,pre,M,cnt]]

    while Q:

        x, y, p, G, c = Q.pop(0)

        if x == 2 and y == 2:
            if G == S:
                if MIN > c:
                    MIN = c
                    return

        for m in range(4):
            tmp = [g[::] for g in G]

            nx = x + di[m]
            ny = y + dj[m]
            if 0<=nx<SIZE and 0<=ny<SIZE:
                if p == -1:
                    tmp[x][y] , tmp[nx][ny] = tmp[nx][ny], tmp[x][y]
                    Q.append([nx, ny,[x,y], tmp, c+1])

                else:
                    if p[0] == nx and p[1] == ny: pass
                    else:
                        tmp[x][y], tmp[nx][ny] = tmp[nx][ny], tmp[x][y]
                        Q.append([nx, ny, [x,y] ,tmp,c+1])





S = [[1,2,3],[4,5,6],[7,8,0]]
M = [list(map(int, input().split())) for _ in  range(SIZE)]
MIN = 0xfffffff
for i in range(SIZE):
    for j in range(SIZE):
        if M[i][j] == 0:
            BFS(i,j,-1,M,0)
            break


if MIN == 0xfffffff:print(-1)
else:print(MIN)
