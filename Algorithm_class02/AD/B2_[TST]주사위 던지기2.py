import sys
sys.stdin = open('input.txt')

def perm(k,n,T):

    if sum(T) > M:
        return
    if k == n:
        if sum(T) == M:
            for t in T:
                print(t, end= ' ')
            print()
        return

    for i in range(6):
        T[k] = arr[i]
        perm(k+1, n, T)
        T[k] = 0

N, M = map(int, input().split())
T = [0]*N
arr = [1,2,3,4,5,6]
perm(0, N, T)


