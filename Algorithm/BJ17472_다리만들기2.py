import sys
sys.stdin = open('input.txt')

dy = [-1,1,0,0]
dx = [0,0,-1,1]


def DFS(row):
    visited[row] = 1
    global MIN

    if sum(visited) == n-1:
        return
    
    for i in range(n-1):
        if met[row][i] and not visited[i]:
            visited[row]
            DFS(i)


def fill_metrix():
    for i in range(R):
        for j in range(C):
            if island[i][j]:
                start = island[i][j]

                for m in range(4):
                    x = i
                    y = j

                    x += dx[m]
                    y += dy[m]

                    while True:
                        if 0<=x<R and 0<=y<C:
                            if island[x][y] == start:
                                break
                            elif not island[x][y]:
                                x += dx[m]
                                y += dy[m]
                            else:
                                end = island[x][y]
                                length = abs(x-i) + abs(y-j) -1
                                if length < 2:
                                    break
                                if not met[start-1][end-1] or met[start-1][end-1] > length:
                                    met[start-1][end-1] = length
                                break

                        else:
                            break

def named_island(i,j,n):
    Q = [(i,j)]
    island[i][j] = n

    while Q:
        x, y = Q.pop(0)
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            if 0<=nx<R and 0<=ny<C and M[nx][ny]:
                M[nx][ny] = 0
                island[nx][ny] = n
                Q.append((nx,ny))


R, C = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(R)]
island = [[0]*C for _ in range(R)]
n = 1
for i in range(R):
    for j in range(C):
        if M[i][j]:
            named_island(i,j,n)
            n+=1


met = [[0]*(n-1) for _ in range(n-1)]

fill_metrix()

visited = [0]*(n-1)
MIN = 0xfffffff
DFS(0)

for x in island:
    print(*x)
print()

for x in met:
    print(*x)
print()

if MIN == 0xfffffff:
    print(-1)
else:
    print(MIN)


