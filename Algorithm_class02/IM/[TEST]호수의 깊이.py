import sys
sys.stdin = open('input.txt')

N = int(input())

M = [list(map(int, input().split())) for _ in range(N)]

Di = [0,0,-1,1]
Dj = [-1,1,0,0]

def DFS(i, j , d, ans):
    global D
    global M

    if M[i][j] == 0:
        return 0
    else:
        while M[i][j] != 0:
            ans += 1
            if 0 <= i + Di[d] < N and 0 <= j + Dj[d] < N:
                i += Di[d]
                j += Dj[d]
                DFS(i, j , d, ans )
    return ans

cnt = 0
for i in range(N):
    for j in range(N):
        if M[i][j] == 1:
            deep = 10000
            for d in range(4):
                # if 0 <= i+D[d] < N and 0 <= j+D[d] < N:
                tmp_deep =  DFS(i, j, d, 0)
                if deep > tmp_deep:
                    deep = tmp_deep
            cnt += deep


print(cnt)


