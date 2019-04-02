import sys
sys.stdin = open('input.txt')

def cut(s,e,h):
    while s <= e:
        m = (s+e)//2
        if tree[m] <= h:
            s = m+1
        else:
            e = m-1
    SUM = 0

    for i in range(e,N):
        if (tree[i] - h) > 0:
            SUM += (tree[i] - h)
    return SUM


def H(s,e):
    global MIN
    while s <= e:
        m = (s+e)//2
        S = cut(0,N-1,m)
        if abs(S - M) < MIN:
            MIN_H = m
            MIN = abs(S - M)
            s = m-1
        else:
            e = m+1




N, M = map(int, input().split())
print(N)
tree = list(map(int, input().split()))
tree.sort()

MIN = 0xfffffff
MIN_H = 0
print(tree)
print(H(0, max(tree)))
print(cut(0,N-1,14))


print(MIN_H)
