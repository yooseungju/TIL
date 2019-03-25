import sys, datetime
sys.stdin = open('input.txt')
import copy

def length(A,k):
    L = 0
    pre = 0

    for a in A[2:k]:
        if M[pre][a] == 0:
            M[pre][a] = abs(data[pre][0] - data[a][0]) + abs(data[pre][1] - data[a][1])
            if pre != 0:
                M[a][pre] = M[pre][a]
        L += M[pre][a]
        pre = a

    if M[pre][1] == 0:
        M[pre][1] = abs(data[pre][0] - data[1][0]) + abs(data[pre][1] - data[1][1])

    L += M[pre][1]

    return L

def perm(k, n):
    global MIN, A
    if len(A[0:k]) > 2 and length(A,k) > MIN:
        return
    if k == n:
        if length(A,k) < MIN:
            MIN = length(A,k)
    else:
        for i in range(k, n):
            A[k] , A[i] = A[i], A[k]
            perm(k+1, n)
            A[k], A[i] = A[i], A[k]


T = 10
start = datetime.datetime.now()
for tc in range(T):
    N = int(input())
    IN = list(map(int, input().split()))
    data = [[IN[(i*2)], IN[(i*2)+1]]for i in range(N+2)]

    A = [j for j in range(N+2)]
    MIN = float('inf')
    M = [[0 for _ in  range(N+2)] for _ in range(N+2)]
    perm(2,N+2)


    print('#{} {}'.format(tc+1, MIN))
print(datetime.datetime.now() - start)