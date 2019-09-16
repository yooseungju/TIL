import sys
sys.stdin = open('input.txt')

def tolist(tmp_M):
    for i in range(N):
        tmp_M[i] = list(tmp_M[i])

re_turn = [0,3,2,1]
def move(tmp_M):
    i = 0
    j = 0
    while i < N:
        cnt = 0
        while j < len(tmp_M[i]):
            if tmp_M[i][j] == 0:
                tmp_M[i].pop(j)
                cnt += 1
            else:
                j+=1
        j = 0
        while j < len(tmp_M[i]):
            if j+1<len(tmp_M[i]) and tmp_M[i][j] == tmp_M[i][j+1]:
                tmp_M[i].pop(j)
                tmp_M[i][j] = (tmp_M[i][j]*2)
                cnt += 1
                j+=1
            else:
                j += 1
        for _ in range(cnt):
            tmp_M[i].append(0)
        j = 0
        i +=1

def mid(tmp_M):
    global MAX
    for t in tmp:
        for n in range(t):
            tmp_M = list(zip(*tmp_M[::-1]))
        tolist(tmp_M)
        move(tmp_M)
        for r in range(re_turn[t]):
            tmp_M = list(zip(*tmp_M[::-1]))

    for m in range(N):
        if MAX < max(tmp_M[m]):
            MAX = max(tmp_M[m])

def perm(n):
    if n == 5:
        tmp_M = [M[i][::] for i in range(N)]
        mid(tmp_M)
        return

    for i in range(4):
        tmp[n] = i
        perm(n+1)
        tmp[n] = 0

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
tmp = [0,0,0,0,0]
MAX = 0
perm(0)
print(MAX)