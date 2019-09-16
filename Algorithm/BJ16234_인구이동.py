import sys
sys.stdin = open('input.txt')

dx = (0,0,-1,1)
dy = (-1,1,0,0)


def BFS(i,j,v):
    Q = [(i,j)]
    visited[i][j] = v

    count = M[i][j]
    n = 1

    while Q:
        x, y = Q.pop(0)

        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            if 0 <= nx < N and 0<= ny < N and not visited[nx][ny] and L <= abs(M[x][y] - M[nx][ny]) <= R:
                count += M[nx][ny]
                n+=1
                visited[nx][ny] = v
                Q.append((nx,ny))

    if n==1:
        visited[i][j] = 0
        return False
    else:
        tmp[v] = count//n
        return True


def merge():
    for i in range(N):
        for j in range(N):
            if visited[i][j] and visited[i][j] in tmp.keys():
                M[i][j] = tmp[visited[i][j]]




N , L, R = map(int, input().split())

M = [list(map(int, input().split())) for _ in range(N)]


Cnt = 0

while 1:

    visited = [[0]*N for _ in range(N)]
    tmp = {}

    v = 1

    for i in range(N):
        for j in range(N):
            if M[i][j] and not visited[i][j]:
                if BFS(i,j,v):
                    v+=1

    if not tmp:
        break
    else:
        merge()
        Cnt += 1

print(Cnt)

