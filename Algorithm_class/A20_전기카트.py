import sys
sys.stdin = open('A20_전기카트_input.txt')


def perm(k, n, SUM):
    global MIN
    if SUM > MIN:
        return
    if k == n:
        if SUM + M[A[-1]][0] < MIN:
            MIN = SUM + M[A[-1]][0]

    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]
            perm(k+1, n, SUM+M[A[k-1]][A[k]])
            A[k], A[i] = A[i], A[k]

T  = int(input())

for tc in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    MIN = 0xfffffff

    perm(1, N, M[0][0])

    print('#{} {}'.format(tc+1, MIN))
