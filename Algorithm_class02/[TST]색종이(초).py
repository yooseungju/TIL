import sys
sys.stdin = open('input.txt')

T = int(input())
M = [[0 for _ in range(100)] for _ in range(100)]

cnt = 0
for _ in range(T):
    i, j = map(int, input().split())

    for y in range(10):
        for x in range(10):
            if M[i+y][j+x] == 0:
                cnt += 1
                M[i + y][j + x] = 1

    M[i][j]

print(cnt)