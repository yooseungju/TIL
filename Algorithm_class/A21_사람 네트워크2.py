import sys
sys.stdin = open('input.txt')

INF = 0xfffffff
T = int(input())
for tc in range(T):
    IN = list(map(int, input().split()))
    N = IN.pop(0)
    D = [[INF]*N for _ in range(N)]
    k = 0

    for i in range(N):
        for j in range(N):
            if IN[k] == 1:
                D[i][j] = 1
            if i ==j:
                D[i][j] = 0
            k +=1


    for k in range(N):
        for i in range(N):
            for j in range(N):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
    MIN = 0xfffffff
    for r in D:
        if sum(r) < MIN:
            MIN = sum(r)
    print('#{} {}'.format(tc+1, MIN))

