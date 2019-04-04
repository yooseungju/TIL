
import sys
sys.stdin = open('input.txt')



def BFS():
    global chk
    # 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4
    dj = (1,-1,0,0)
    di = (0,0,1,-1)
    Q=[(sx-1,sy-1,sd-1)]

    while Q:
        x,y,d = Q.pop(0)
        if x == ex-1 and y == ey-1 and d == ed-1:
            print(chk[x][y][d])
            return

        for i in range(1,4):
            nx = x + i*di[d]
            ny = y + i*dj[d]
            if 0 <= nx < M and 0 <= ny<N and not arr[nx][ny]:
                if not chk[nx][ny][d]:
                    Q.append((nx,ny, d))
                    chk[nx][ny][d] = chk[x][y][d] + 1
            else:
                break


        for i in range(4):
            if i == d:
                continue

            k = 2 if (i+d)%4 == 1 else 1
            if not chk[x][y][i]:
                Q.append((x,y,i))
                chk[x][y][i] = chk[x][y][d] + k



# 세로 가로
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
chk = [[[0]*4 for _ in range(N)] for _ in range(M)]
sx, sy, sd =  map(int, input().split())
ex, ey, ed =  map(int, input().split())
cnt = 0

BFS()
