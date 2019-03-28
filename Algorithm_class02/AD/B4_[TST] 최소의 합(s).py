import sys
sys.stdin = open('input.txt')


def rePerm(k, n , sum):
    global  Min
    if sum > Min:
        return
    if k == n:
        if Min > sum:
            Min = sum
    else:
        for i in range(N):
            rePerm(k+1, n, sum+M[k][i])


def Perm(k, n , sum):
    global  Min
    if sum > Min:
        return
    if k == n:
        if Min > sum:
            Min = sum
    else:
        for i in range(N):
            if not chk[i]:
                chk[i] = 1
                Perm(k+1, n, sum+M[k][i])
                chk[i] = 0



N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

Min = 0xfffffff
rePerm(0, N, 0)
print(Min)

chk = [0]*N
Min = 0xfffffff
Perm(0,N,0)
print(Min)
