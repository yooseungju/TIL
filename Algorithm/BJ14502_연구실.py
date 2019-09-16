import sys
sys.stdin = open('input.txt')



dy = (-1,1,0,0,-1,-1,1,1)
dx = (0,0,-1,1,-1,1,-1,1)



def BFS():
    global MAX
    q = [i[:] for i in Q]
    visited = [[0]*c for _ in range(r)]
    count = 0

    for s in q:
        a, b = s
        visited[a][b] = 1

    while q:
        x,y = q.pop(0)
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]

            if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and not M[nx][ny]:
                visited[nx][ny] = 1
                count += 1
                q.append((nx,ny))

                if non - count < MAX:
                    return

    if non-count > MAX:
        MAX = (non-count)


def build(n,x,y):
    if n == 3:
        BFS()
        return

    for i in range(x,r):
        for j in range(y,c):
            if not M[i][j]:
                M[i][j] = 1
                build(n+1,i,j+1)
                M[i][j] = 0
        y = 0

r, c = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(r)]


MAX = 0
non = -3

Q = []
for i in range(r):
    for j in range(c):
        if M[i][j] == 2:
            Q.append((i,j))
        elif M[i][j] == 0:
            non += 1
build(0,0,0)
print(MAX)