import sys
sys.stdin = open('input.txt')

def change(x, y, s, d):
    dj = [0, 0, 0, 1, -1]
    di = [0, -1, 1, 0, 0]

    nx = x + di[d]*s
    ny = y + dj[d]*s

    while True:
        if 0 <= nx < R and 0 <= ny < C:
            return nx, ny, d
        #상 초과
        if nx >= R:
            nx = (R - 1) - (nx - (R - 1))
            d = 1

        #하 초과
        if nx < 0:
            nx =  abs(nx)
            d = 2

        #우 초과
        if ny >= C:
            ny = (C - 1) - (ny - (C - 1))
            d = 4

        # 좌 초과
        if ny < 0:
            ny = abs(ny)
            d = 3


def move():
    # 1 위 , 2  아래,  3  오른쪽 , 4 왼쪽
    dj = [0,0,0,1,-1]
    di = [0,-1,1,0,0]

    for x in range(R):
        for y in range(C):
            if G[x][y] != 0:
                s, d, z = G[x][y]



                nx, ny, d = change(x,y,s,d)

                if visited[nx][ny]  ==  0:
                    visited[nx][ny] = (s,d,z)

                else:
                    s1, d1, z1 = visited[nx][ny]

                    if z1 < z:
                        visited[nx][ny] = (s,d,z)

count = 0
R , C,  M = map(int, input().split())
if M > 0:
    G = [[0]*C for _ in range(R)]


    for _ in range(M):
        r, c ,s, d, z = map(int, input().split())
        G[r-1][c-1] = (s,d,z)




    for f_k in range(C):
        visited = [[0] * C for _ in range(R)]
        for i in range(R):
            if G[i][f_k]  !=  0:
                s,d,z = G[i][f_k]
                count += z
                G[i][f_k] = 0
                break


        move()



        for i in range(R):
            for j in range(C):
                G[i][j] = visited[i][j]





print(count)