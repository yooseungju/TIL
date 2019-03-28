import sys
sys.stdin = open('input.txt')



def perm(k, n, sum):
    global Min
    if sum > Min:
        return
    if k ==n:
        if Min > sum:
            Min = sum
    else:
        for i in range(N):
            if chk[i] == 0:
                chk[i] = 1
                perm(k+1, n, sum+M[k][i])
                chk[i] = 0


N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
Min = 0xfffffff
chk = [0]*N
perm(0, N, 0)
print(Min)


