import sys

sys.stdin = open('input.txt')

def SUM(n):
    if n <= 1:
        return 1
    else:
        return n + SUM(n-1)




N = int(input())
M = [0]*N
print(SUM(N))