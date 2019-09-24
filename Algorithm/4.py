import sys
sys.stdin = open('input.txt')



def solution(s,e,j):
    me = [0] * N

    for i in range(s,e,j):
        for m in range(2):
            ni = i + -(j)
            if 0 <= ni <N:
                if M[i]:
                    me[i] = 0
                else:
                    me[i] = me[ni] + 1
    return me

N = int(input())
M = list(map(int,input().split()))


pre = M[0]
cnt = 0
for i in range(1,N):
    if M[i] != pre:
        pre = M[i]
        cnt += 1

if cnt > 1:
    a = solution(0,N,1)
    b = solution(N-1,-1,-1)

    tmp = [0]*N

    for i in range(N):
        tmp[i] = min(a[i], b[i])
    print(max(tmp))

else:
    a = solution(0, N, 1)
    b = solution(N - 1, -1, -1)

    tmp = [0] * N

    for i in range(N):
        tmp[i] = max(a[i], b[i])

    print(max(tmp))
