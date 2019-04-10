import sys
sys.stdin = open('input.txt')


N = int(input())

IN = list(map(int, input().split()))



IN.sort()
i = 0
f = 1

SUM = 0
while 0 <= i < N:
