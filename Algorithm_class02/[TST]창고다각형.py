import sys
sys.stdin = open('input.txt')


def area(pre, pivot, post):
    count = 0
    Max = 0
    global M
    index = 0
    while index < pivot[0]:
        for m in M:
            



N = int(input())
M = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda m: m[0])


pre = M[0]
pivot = max(M , key = lambda m:m[1])[:]
post = M[-1][:]



print(area(pre, pivot, post))



