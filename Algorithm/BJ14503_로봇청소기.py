import sys
sys.stdin = open('input.txt')


#0:북쪽에서 왼쪽은 좌 ,1: 동쪽에서 왼쪽은 상, 2: 남쪽에서 왼쪽은 우,3: 서쪽에서 왼쪽은 하
# 좌 상 우 하
dy = (-1,0,1,0)
dx = (0,-1,0,1)

#북쪽에서 뒤쪽은 하 ,동쪽에서 뒤쪽은 좌, 남쪽에서 뒤는 상, 서쪽에서 뒤쪽은 우
back = {0:3,1:0,2:1,3:2}


turn = [0,1,2,3]

def BFS(i,j,d):
    global cnt
    Q = [(i,j,d)]
    cnt += 1
    M[i][j] = 2

    while Q:
        x, y, d = Q.pop(0)

        count = 4

        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            if not M[nx][ny]:
                cnt += 1
                M[nx][ny] = 2
                Q.append((nx,ny,turn[d-1]))
                break
            else:
                count -= 1
                d = turn[d-1]

                if not count:
                    break

        if not count:
            b = back[d]

            nx = x + dx[b]
            ny = y + dy[b]
            if not(0<=nx<r and 0<=ny<c) or M[nx][ny] == 1:
                return

            M[nx][ny] = 2
            Q.append((nx,ny,d))

r, c = map(int, input().split())
x, y, d = map(int, input().split())
visited = [[0]*c for _ in range(r)]
M = [list(map(int, input().split())) for _ in range(r)]
cnt = 0

BFS(x,y,d)

print(cnt)

