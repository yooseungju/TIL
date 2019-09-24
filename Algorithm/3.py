import sys
sys.stdin = open('input.txt')

M = [0]*200
N = int(input())

for _ in range(N):
    s, e = map(int,input().split())

    for i in range(s,e):
        M[i] += 1

print(max(M))
