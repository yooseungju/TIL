import sys
sys.stdin = open('input.txt')


def BFS(i,j,Sum):
    global MIN
    #시계 방향 탐색
    dj = [1,0]
    di = [0,1]
    S = [[i, j, Sum]]
    while S:
        x,y,SUM= S.pop()
        if x == N-1 and y == N-1:
            if SUM < MIN:
                MIN = SUM
        for m in range(2):
            nx = x+di[m]
            ny = y+dj[m]
            if 0 <= nx< N and 0 <= ny < N:
                S.append([nx,ny,SUM+M[nx][ny]])


N = int(input())
M = [list(map(int, list(input()))) for _ in range(N)]
rec = [[0xfffffff]*N for _ in range(N)]
MIN = 0xfffffff
BFS(0,0,0)
print(MIN)