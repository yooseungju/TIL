import sys
sys.stdin = open('input.txt')

dx = (0,0,-1,1)
dy = (-1,1,0,0)

def check(i,j,all):
    visited = [[0] * C for _ in range(R)]
    visited[i][j] = 1
    q = [(i, j)]

    remain = 1
    while q:
        x, y = q.pop(0)
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            if 0 <= nx < R and 0 <= ny < C and M[nx][ny] and not visited[nx][ny]:
                remain += 1
                visited[nx][ny] = 1
                q.append((nx,ny))

    if all != remain:
        return True
    else:
        return False


def melt():
    global count
    cut = {}

    while Q:
        x,y = Q.pop(0)
        c = 0
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            if 0<= nx< R and 0<=ny < C and not M[nx][ny]:
                c +=1
        cut[(x,y)] = c



    for k, v in cut.items():
        i,j = k
        if M[i][j] - v > 0:
            M[i][j] -= v
            Q.append(k)
        else:
            M[i][j] = 0

    all = len(Q)

    if not all:
        count = 0
        return True

    x,y = Q[0]

    return check(x,y,all)


R , C = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(R)]


Q = []

for i in range(1,R):
    for j in range(1,C):
        if M[i][j]:
            Q.append((i, j))

count = 0
while 1:
    count += 1
    if melt():
        break
print(count)









