import sys
from collections import deque
sys.stdin = open("input.txt")

T = int(input())



def BFS():
    Q = deque([(0, 0)])
    visited[0][0] = True
    d[0][0] = Map[0][0]

    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    while len(Q) > 0:
        x, y = Q.popleft()

        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] or  d[nx][ny] > d[x][y] + Map[nx][ny]:
                    d[nx][ny] = d[x][y] + Map[nx][ny]
                    Q.append((nx,ny))
                    visited[nx][ny] = True



for tc in range(T):
    N = int(input())
    Map = [list(map(int, list(input()))) for _ in range(N)]

    visited = [[False for _ in range(N)] for _ in range(N)]
    d = [[999999 for _ in range(N)] for _ in range(N)]

    BFS()

    print(f"#{tc+1} {d[N-1][N-1]}")
