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
    print('che')
    global MM
    global cnt
    i += 1
    for p in range(1,P):
        if MM[i][j:j+P] == PM[p]:
            i += 1
        else:
            return
    return True


while Mi < M-P:
    while Mj < M-P:
        if MM[Mi][Mj:Mj+P] == PM[0]:
            if check(Mi, Mj, P):
                Mi = -1
                Mj = -1

        Mj += 1
    Mi += 1

print(cnt)





