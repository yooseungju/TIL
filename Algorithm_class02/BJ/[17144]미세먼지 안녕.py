import sys

sys.stdin = open('input.txt')


def move():
    uj = [1,0,-1,0]
    ui = [0,-1,0,1]
    dummy = [(uX,C-1),(0,C-1),(0,0)]
    x = uX
    y = uY

    pre = 0
    c = 0
    while True:
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
    dummy = [(dX, C-1), (R-1, C-1), (R-1, 0)]
    x = uX + 1
    y = uY
    pre = 0
    c = 0

    while True:
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
    #
    # for i in range(R):
    #     for j in range(C):
    #         print(M[i][j], end=' ')
    #
    #     print()
    # print()

    return


R, C, T = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(R)]
clear = []

for i in range(R):
    for j in range(C):
        if M[i][j] == -1:
            clear.append((i,j))


uX, uY = clear[0]
dX, dY = clear[1]



dj = [-1,1,0,0]
di = [0,0,-1,1]

while  T>0:
    visited = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if M[i][j] > 0:
                n = 0
                for m in range(4):
                    nx = i + di[m]
                    ny = j + dj[m]

                    if 0 <= nx < R and 0 <= ny < C:
                        if M[nx][ny] != -1:
                            e = M[i][j] // 5
                            visited[nx][ny] += e
                            n+=1
                if n > 0:
                    M[i][j] -= (M[i][j]//5)*n

    for i in range(R):
        for j in range(C):
            if visited[i][j] > 0:
                M[i][j] += visited[i][j]

    move()
    T-=1


SUM = 0
for i in range(R):
    for j in range(C):
        if M[i][j] > 0:
            SUM += M[i][j]

print(SUM)
