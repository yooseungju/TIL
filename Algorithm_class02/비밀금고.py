import sys
sys.stdin = open('input.txt')

N = int(input())

M = [[0 for _ in range(N*2-1)] for _ in range(N*2-1)]

L = list(map(int, input().split()))

a = 1
one = 1

for i in range(N*2-1):
    first_idx = N-a
    for j in range(a):
        M[i][first_idx+2*j] = L.pop(0)
    if a == N:
        one = -one
    a += one

M = list(zip(*M[::-1]))

MAX = 0
for m in range(N*2-1):
    if MAX < sum(M[m]):
        MAX = sum(M[m])

print(MAX)