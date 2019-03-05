import sys
sys.stdin = open('input.txt')

N =int()

M = [[0 for _ in range(N)] for _ in range(N)]
value = 1
i = 0
j = 0

while i < N:
    while j < N:
        M[i][j]