import sys
sys.stdin = open('input.txt')

dx = (0,0,1,-1,0,0)
dy = (1,-1,0,0,0,0)
dz = (0,0,0,0,-1,1)

def BFS(S):
    q,i,j = S
    visited[q][i][j] = 1
    Q = [(q,i,j)]

    while Q:
        z,x,y = Q.pop(0)

        for m in range(6):
            nz = z + dz[m]
            nx = x + dx[m]
            ny = y + dy[m]

            if 0<=nz<L and 0<=nx<R and 0<=ny<C and M[nz][nx][ny] !="#" and (visited[nz][nx][ny] == 0 or visited[nz][nx][ny] > visited[z][x][y] + 1):
                Q.append((nz,nx,ny))
                visited[nz][nx][ny] = visited[z][x][y] + 1
                if (nz,nx,ny) == E:
                    print("Escaped in {} minute(s).".format(visited[nz][nx][ny]-1))
                    return

    print("Trapped!")

while 1:
    L, R, C = map(int, input().split())
    if not L and not R and not C:
        break

    M = []

    visited = [[[0]*C for _ in range(R)] for _ in range(L)]

    for l in range(L*2):
        if l % 2 == 0:
            M.append([list(input()) for _ in range(R)])
        else:
            input()

    S = 0
    E = 0

    for z in range(L):
        for x in range(R):
            for y in range(C):
                if M[z][x][y] == "S":
                    S = (z,x,y)
                elif M[z][x][y] == "E":
                    E = (z,x,y)

    BFS(S)