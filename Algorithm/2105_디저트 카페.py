import sys
sys.stdin = open("input.txt")
# 우하 좌하 좌상 우상
dy = (1, -1, -1, 1)
dx = (1, 1, -1, -1)


def check(x, y):
    global Max
    tmp = []
    c = 0

    for i in range(4):
        for j in range(num[i]):
            x = x + dx[i]
            y = y + dy[i]
            if not M[x][y] in tmp:
                tmp.append(M[x][y])
                c += 1
            else:
                return
    if Max < c:
        Max = c

def DFS(n, x, y, k, r):
    if n > 2:
        if num[0] != num[2]:
            return

    if n == 4:
        if num[0] == num[2] and num[1] == num[3]:
            check(k, r)
        return

    for i in range(N, 0, -1):
        nx = x + (dx[n] * i)
        ny = y + (dy[n] * i)

        if 0 <= nx < N and 0 <= ny < N:
            num[n] = i
            DFS(n + 1, nx, ny, k, r)

T = int(input())
for tc in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]

    num = [0, 0, 0, 0]
    Max = -1

    for i in range(N):
        for j in range(N):
            DFS(0, i, j, i, j)

    print("#{} {}".format(tc + 1, Max))