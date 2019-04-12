import sys
sys.stdin = open('input.txt')




def BFS(i,j):
    global visited
    flag = 0
    dj = (-1, 1, 0, 0)
    di = (0, 0, -1, 1)
    visited[i][j] = 1
    Q = [(i,j)]
    SUM = M[i][j]
    c = 1

    while len(Q) > 0:
        x, y = Q.pop(0)
        for m in range(4):
            nx = x + di[m]
            ny = y + dj[m]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if L <= abs(M[x][y] - M[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    flag = 1
                    Q.append((nx,ny))
                    SUM += M[nx][ny]
                    c += 1

    AVG = SUM//c

    if flag:
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1:
                    visited[i][j] = 2
                    M[i][j] = AVG

    return flag



def solution():
    global visited
    ans = 0
    cnt  = 0
    flag = False

    while True:
        if flag:
            ans += 1
            flag = False

        visited = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    f = BFS(i,j)
                    if f:
                        flag = True
                        cnt = 0
                    else:
                        visited[i][j] = 0
                        cnt += 1

            if i == N-1 and j == N-1:
                if flag == False:
                    return ans


N, L, R = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
print(solution())