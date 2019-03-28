import sys
sys.stdin = open('input.txt')

SIZE = 100

T = int(input())
M = [[0 for _ in range(SIZE+1)] for _ in range(SIZE+1)]


cnt = 0
for _ in range(T):
    i, j = map(int, input().split())

    for y in range(10):
        for x in range(10):
            if M[i+y][j+x] == 0:
                M[i + y][j + x] = 1



di = [0,0,-1,1]
dj = [-1,1,0,0]

for y in range(SIZE):
    for x in range(SIZE):
        if M[y][x] == 1:
            if y == 0 or y == len(M)-1 or x == 0 or x == len(M)-1:
                cnt += 1
            for m in range(4):
                if 0 <= y+di[m] < 100 and 0 <= x+dj[m] < len(M):
                    if M[y+di[m]][x+dj[m]] == 0:
                        cnt += 1

print(cnt)



