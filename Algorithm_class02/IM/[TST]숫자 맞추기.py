import sys
sys.stdin = open('input.txt')

N = int(input())

game = [[0 for i in range(N)] for _ in range(3)]

i = 0

while i < N:
    a, b, c = map(int, input().split())
    game[0][i] = a
    game[1][i] = b
    game[2][i] = c
    i += 1
count = [0 for _ in range(N)]



for i in range(3):
    for j in range(N):
        if game[i][j] != 0 and game[i].count(game[i][j]) > 1:
            game[i] = [0 if c == game[i][j] else c for c in game[i]]

    for x in range(N):
        count[x] += game[i][x]

for y in range(N):
    print(count[y])