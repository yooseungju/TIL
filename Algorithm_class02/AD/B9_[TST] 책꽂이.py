import sys
sys.stdin = open('input.txt')

T = int(input())


def power_set(k,n,SUM):
    global MIN

    if k == n:
        if SUM >= B and SUM < MIN:
            MIN = SUM
    else:
        power_set(k+1, n, SUM+H_i[k])
        power_set(k+1, n, SUM)

for _ in range(T):

    N , B = map(int, input().split())

    H_i =[int(input()) for _ in range(N)]
    MIN = 0xfffffff
    power_set(0, N, 0)
    print(MIN-B)

