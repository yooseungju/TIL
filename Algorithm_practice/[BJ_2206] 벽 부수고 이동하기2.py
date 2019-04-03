import sys
sys.stdin  = open('input.txt')

def BFS():
    # 4방향 탐색
    dj = [-1,1,0,0]
    di = [0,0,-1,1]
    Q = [[0,0,0]]
    visited[0][0][0] = 1
    while Q:
        x,y,z = Q.pop(0)
        if x == N-1 and y == M-1:
            return visited[x][y][z]

        for m in range(4):
            nx = x+di[m]
            ny = y+dj[m]

            if 0 <= nx <N and 0 <= ny <M:

                if G[x + di[m]][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z]+1
                    Q.append([nx,ny,z])

                elif G[nx][ny] == 1:
                    if z == 0 and visited[nx][ny][1] == 0:
                        visited[nx][ny][1] = visited[x][y][z]+1
                        Q.append([nx, ny, z+1])
    return



N, M = map(int , input().split())
G = [list(map(int,list(input()))) for _ in range(N)]
visited = [[[0]*2 for _  in range(M)] for _ in range(N)]
ans = BFS()
if ans == None:print(-1)
else:print(ans)