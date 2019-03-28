import sys
sys.stdin = open('input.txt')




def com(k ,n , Sum):
    global ans, chk
    if ans == 'YES':
        return
    if Sum > K:
        return
    if k == n:
        if Sum == K:
            ans = 'YES'
        return
    else:
        chk[k] = 0
        com(k+1, n, Sum+M[k])
        chk[k] = 0
        com(k + 1, n, Sum)


T = int(input())
for _ in range(T):
    N , K = map(int, input().split())
    M = list(map(int, input().split()))
    ans = 'NO'


    chk = [0]*N
    ME = []

    com(0, N, 0)
    print(ans)




