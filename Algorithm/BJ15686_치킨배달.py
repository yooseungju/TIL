import sys, itertools
sys.stdin = open('input.txt')


def check():
    global MIN
    count = 0
    for h in home:
        x1, y1 = h
        Min = 0xfffffff
        for t in tmp:
            x2, y2 = t
            length = abs(x1-x2) + abs(y1-y2)
            if length < Min :
                Min = length
        count += Min

    if count < MIN:
        MIN = count

def com(n, s):
    if n == C:
        check()
        return
    for i in range(s, len(chikens)):
        tmp[n] = chikens[i]
        com(n+1,i+1)
        tmp[n] = 0


N, C = map(int, input().split())

M = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]


home = []
chikens = []

for i in range(N):
    for j in range(N):
        if M[i][j] == 1:
            home.append((i,j))
            visited[i][j] = 1
        elif M[i][j] == 2:
            chikens.append((i,j))
MIN = 0xfffffff
tmp = [0]*C
com(0,0)

print(MIN)

