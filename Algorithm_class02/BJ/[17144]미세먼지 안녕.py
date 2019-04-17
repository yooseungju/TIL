import sys

sys.stdin = open('input.txt')


def move():

    uj = [1,0,-1,0]
    ui = [0,-1,0,1]

    dummy = [(uX,C-1),(0,C-1),(0,0),(uX,uY)]

    x = uX
    y = uY

    pre = 0
    c = 0
    while c < 4:
        x += ui[c]
        y += uj[c]
        if x==uX and y==uY:
            break

        if 0<=x<R and 0<=y<C:
            tmp =  M[x][y]
            M[x][y] = pre
            pre = tmp

        if (x,y) in dummy:
            c += 1




    dj = [1, 0, -1, 0]
    di = [0, 1, 0, -1]

    dummy = [(dX, C-1), (R-1, C-1), (R-1, 0), (uX, uY)]

    x = uX + 1
    y = uY

    pre = 0
    c = 0

    while c < 4:
        x += di[c]
        y += dj[c]
        if x==dX and y==dY:
            break

        if 0<=x<R and 0<=y<C:
            tmp =  M[x][y]
            M[x][y] = pre
            pre = tmp

        if (x,y) in dummy:
            c += 1

    for i in range(R):
        for j in range(C):
            print(M[i][j], end=' ')
        print()
    print()








def BFS(Q):
    visited = [[0] * C for _ in range(R)]

    cnt = 0
    dj = [-1,1,0,0]
    di = [0,0,-1,1]

    while len(Q) > 0:
        x,y = Q.pop(0)

        if x == 1001:

            for i in range(R):
                for j in range(C):
                    M[i][j] += visited[i][j]

            move()

            Q.append((1001,1001))
            cnt += 1
            visited = [[0] * C for _ in range(R)]




            if cnt == T:

                return
            continue
        n = 0
        for m in range(4):

            nx = x + di[m]
            ny = y + dj[m]

            if 0<=nx<R and 0<=ny<C:
                if M[nx][ny] != -1:
                    n += 1
                    e = M[x][y]//5
                    visited[nx][ny] += e


        if n > 0:
            M[x][y] -= (M[x][y]//5)*n



R, C, T = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(R)]
clear = []
dust = []

for i in range(R):
    for j in range(C):
        if M[i][j] == -1:
            clear.append((i,j))
        elif M[i][j] != 0:
            dust.append((i,j))


uX, uY = clear[0]
dX, dY = clear[1]

dust.append((1001,1001))
BFS(dust)
SUM = 0


for i in range(R):
    for j in range(C):
        if M[i][j] != -1:
            SUM += M[i][j]

print(SUM)
