import sys
sys.stdin = open('input.txt')

def check_closs(x, y, num):
    dj = [-1, -1, 1, 1]
    di = [-1, 1, -1, 1]


    for d in range(4):
        xt = x
        yt = y
        while xt + di[d] >= 0 and xt + di[d] < N and yt + dj[d] >= 0 and yt + dj[d] < N:
            xt += di[d]
            yt += dj[d]
            closs_chk[xt][yt] +=  num

def perm(k, n, cnt):
    global MAX

    if k == n:
        if cnt == N:
            MAX +=1
    else:
        flag = False
        for i in range(N):
            if not chk[i] and not closs_chk[k][i]:
                flag = True
                chk[i] = 1
                closs_chk[k][i] = 1
                check_closs(k,i,1)

                perm(k+1, n, cnt+1)

                chk[i] = 0
                closs_chk[k][i] = 0
                check_closs(k,i,-1)

        if not flag:
            perm(k + 1, n, cnt)

N = int(input())
MAX = 0
chk = [0]*N
closs_chk = [[0]*N for _ in range(N)]
perm(0,N,0)
print(MAX)


