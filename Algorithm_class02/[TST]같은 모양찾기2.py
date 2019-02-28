import sys
sys.stdin = open('input.txt')
M = int(input())
MM = [list(input()) for _ in range(M)]
P = int(input())
PM = [list(input()) for _ in range(P)]


Mi = 0
Mj = 0

Pi = 0
Pj = 0

cnt = 0

def check(i , j, P):
    global MM
    global cnt
    i += 1
    for p in range(1,P):
        if MM[i][j:j+P] == PM[p]:
            i += 1
        else:
            return False
    return True


for _ in range(4):
    while Mi < M-P+1:
        while Mj < M-P+1:
            if MM[Mi][Mj:Mj+P] == PM[0]:
                if check(Mi, Mj, P):
                    cnt += 1
            Mj += 1
        Mj = 0
        Mi += 1
    Mi = 0

    Q = [[0 for _ in range(P)]for _ in range(P)]
    for x in range(P):
        for y in range(P):
            Q[y][P-1-x] = PM[x][y]

    PM = Q

print(cnt)