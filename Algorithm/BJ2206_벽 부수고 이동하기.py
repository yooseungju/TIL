import sys
sys.stdin = open('input.txt')




dy = (-1,1,0,0)
dx = (0,0,-1,1)

def BFS():
    global MIN

    Q = [(0,0,0)]

    visited[0][0][0] = 1


    while Q:
        x, y, c = Q.pop(0)
        if x == R - 1 and y == C - 1:
            MIN = visited[x][y][c]
            return


        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]

            if 0<=nx<R and 0<=ny<C:

                if not M[nx][ny] and not visited[nx][ny][c]:
                    visited[nx][ny][c] = visited[x][y][c]+ 1
                    Q.append((nx,ny,c))

                elif not c and not visited[nx][ny][1]:
                    visited[nx][ny][1] = visited[x][y][c]+ 1
                    Q.append((nx,ny,1))



R , C = map(int, input().split())
M = [list(map(int, list(input()))) for _ in range(R)]
visited = [[[0]*2 for _ in range(C)] for _ in range(R)]
MIN = 0xfffffff

BFS()

if MIN == 0xfffffff:
    print(-1)
else:
    print(MIN)