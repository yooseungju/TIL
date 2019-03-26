import sys
sys.stdin = open('A20_최소합_input.txt')

T = int(input())


def perm(k , n, Sum):
    global sum_min
    if Sum > sum_min:
        return

    if k == n and Sum < sum_min:
            sum_min = Sum
            return
    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]
            perm(k + 1, n, Sum + M[k][A[k]])
            A[k], A[i] = A[i], A[k]

for tc in range(T):
    N = int(input())

    M = [list(map(int, input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    sum_min = 0x7fffffff
    perm(0, N, 0)
    print('#{} {}'.format(tc+1, sum_min,0 ))