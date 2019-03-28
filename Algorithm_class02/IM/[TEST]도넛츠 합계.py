import sys
sys.stdin = open('input.txt')


def doughnut(i, j, K):
    dj = [1, 0, -1, 0]
    di = [0, 1, 0, -1]
    sum = 0
    m = 0
    while m < 4:
        k = 0
        while k < K:
            sum += M[i][j]
            if k + 1 >= K:
                m += 1
                if m == 4:
                    return sum
            i += di[m]
            j += dj[m]
            k += 1
        if m == 1:
            K -= 1
        elif m == 3:
            K -= 1


N, K = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(N)]
Max = 0

for i in range(0, N - 2):
    for j in range(0, N - 2):
        Sum = doughnut(i, j, K)
        if Max < Sum:
            Max = Sum
print(Max)




