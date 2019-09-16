import sys
sys.stdin = open('input.txt')
def check():
    for y in range(C):
        k = y
        for x in range(R):
            if M[x][k] == [0, 1]:
                k += 1
            elif M[x][k] == [1, 0]:
                k -=1

        if k != y:
            return False
    return True


def com(n, sr, sc):
    global MIN

    if MIN <= n:
        return

    if check():
        if MIN > n:
            MIN = n

    if n == 3:
        return

    j = sc
    for i in range(sr, R):
        while j < C - 1:
            if M[i][j] == [0, 0] and M[i][j + 1] == [0, 0]:
                M[i][j] = [0, 1]
                M[i][j + 1] = [1, 0]
                com(n + 1, i, j + 2)
                M[i][j] = [0, 0]
                M[i][j + 1] = [0, 0]
            j += 1
        j = 0


C, N, R = map(int, input().split())
M = [[[0] * 2 for _ in range(C)] for _ in range(R)]

for _ in range(N):
    a, b = map(int, input().split())
    M[a - 1][b - 1][1] = 1
    M[a - 1][b][0] = 1

MIN = 4
com(0, 0, 0)
if MIN < 4:
    print(MIN)
else:
    print(-1)