import sys
sys.stdin = open('input.txt')

N = int(input())

M = [list(map(int, list(input()))) for _ in range(N)]


def ans(r, c):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    for i in range(N):
        for j in range(N):
            if i < r and j < c:
                sum1 += M[i][j]
            elif i < r and j >= c:
                sum2 +=M[i][j]
            elif i >= r and j < c:
                sum3 += M[i][j]
            elif i >= r and j >=c:
                sum4 +=M[i][j]
    if sum1 == sum2 == sum3 == sum4:

        return 1
    else: return 0


SUM = 0
for r in range(1, N):
    for c in range(1, N):
        SUM += ans(r, c)

if SUM == 0:
    print(-1)
else:
    print(SUM)


