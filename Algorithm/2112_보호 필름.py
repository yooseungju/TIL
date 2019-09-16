import sys
sys.stdin = open('input.txt')


def check():
    ch = {i:1 for i in range(W)}

    for j in range(W):
        pre = tmp_M[0][j]
        for i in range(1,D):
            if pre == tmp_M[i][j]:
                ch[j] += 1
                if ch[j] >=K:
                    break
            else:
                ch[j] = 1
            pre = tmp_M[i][j]

        if ch[j] < K:
            return False
    return True

def com2(n,k):
    global Min
    if Min != 0xfffffff:
        return
    if n == k:
        if check():
            Min = k
        return
    tmp_n = tmp[n]
    tmp_M[tmp_n] = [0] * W
    com2(n+1,k)
    tmp_M[tmp_n] = [1] * W
    com2(n+1,k)
    tmp_M[tmp_n] = M[tmp_n][:]

def com(n, start,k):
    if Min != 0xfffffff:
        return
    if n == k:
        com2(0,k)
        return
    for s in range(start, D):
        tmp[n] = s
        com(n+1, s+1, k)

T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(D)]
    tmp_M = [M[i][:] for i in range(D)]

    Min = 0xfffffff
    if K==1 or check():
        Min = 0
    else:
        for i in range(1, D + 1):
            tmp = [0] * i
            com(0, 0, i)
    print("#{} {}".format(tc+1,Min))