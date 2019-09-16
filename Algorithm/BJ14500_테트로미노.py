import sys
sys.stdin = open('input.txt')

# 좌 우 상 하
dy = (1,-1,0,0)
dx = (0,0,-1,1)

e = (1,3)
def exept(i,j):
    global MAX
    for m in range(4):
        x = i
        y = j
        cnt = M[i][j]

        for d in range(2):
            nx = x+(dx[e[d]-m])
            ny = y+(dy[e[d]-m])

            if 0<=nx<r and 0<= ny<c:
                cnt += M[nx][ny]
                x = nx
                y = ny
            else:
                break

        nx = i + 2*dx[1-m]
        ny = j + 2*dy[1-m]

        if 0 <= nx < r and 0 <= ny < c:
            cnt += M[nx][ny]
            if cnt > MAX:
                MAX = cnt



def check(x,y, n, cnt):
    global MAX

    if n == 3:
        if cnt > MAX:
            MAX = cnt
        return

    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]

        if 0<=nx<r and 0<=ny<c and not visitd[nx][ny]:
            visitd[nx][ny] = 1
            check(nx, ny, n+1, cnt+M[nx][ny])
            visitd[nx][ny] = 0


r, c = map(int, input().split())

M = [list(map(int, input().split())) for _ in range(r)]
MAX = 0
visitd = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        visitd[i][j] = 1
        check(i,j,0,M[i][j])
        visitd[i][j] = 0
        exept(i,j)

print(MAX)