import sys
sys.stdin = open('input.txt')

T = int(input())


def perm(k, n, SUM):
    global MIN
    if SUM >  MIN:
        return
    if k == n:
        if SUM < MIN:
            MIN = SUM
            return
    else:
        for i in range(n):
            if chk[i] == 0:
                chk[i] = 1
                perm(k+1, n, SUM+table[k][i])
                chk[i] = 0


for tc in range(T):
    N = int(input())

    SL = list(map(int, input().split()))
    RL = list(map(int, input().split()))
    table = [[0]*N for _ in range(N)]


    for r in range(0,N*2,2):
        for s in range(0,N*2,2):
            table[r//2][s//2] = abs(RL[r]-SL[s]) + abs(RL[r+1]-SL[s+1])


    chk = [0]*N
    MIN = 0xfffffff
    perm(0,N,0)

    print(MIN)

