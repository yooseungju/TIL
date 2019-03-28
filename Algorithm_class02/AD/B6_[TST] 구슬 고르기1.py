import sys
sys.stdin = open('input.txt')


def com(k, n):
    if k == n:
        for i in T[1:]:
            print(i, end=' ')
        print()
        return
    else:
        for i in [k, 0]:
            T[k] = i
            com(k+1,n)

N = 3
T = [0]*(N+1)
arr = [0,1,2,3]
com(1, N+1)
