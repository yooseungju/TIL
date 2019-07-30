import sys
sys.stdin = open("input.txt")

T = int(input())
SIZE = 4

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def BFS(i,j,s):
    Q = [(i,j,s)]
    while len(Q) > 0:
        x,y,s = Q.pop(0)

        if len(s) == 7:
            if s not in tmp:
                tmp.append(s)

        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]

            if 0<= nx < SIZE and 0<= ny < SIZE and len(s) < 7:
                Q.append((nx, ny, s+M[nx][ny]))

for tc in range(T):
    M = [input().split() for _ in range(SIZE)]
    tmp = []
    for i in range(SIZE):
        for j in range(SIZE):
            BFS(i,j,M[i][j])

    print(f"#{tc+1} {len(tmp)}")