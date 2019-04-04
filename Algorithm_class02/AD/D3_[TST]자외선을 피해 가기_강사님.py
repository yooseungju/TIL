import sys
sys.stdin = open('input.txt')


def BFS():

    #시계 방향 탐색
    dj = [1,0,-1,0]
    di = [0,1,0,-1]

    Q = [(0,0)]
    rec[0][0] =  arr[0][0]

    while Q:
        r,c= Q.pop(0)
        for m in range(4):
            nr = r+di[m]
            nc = c+dj[m]
            if 0 <= nr< N and 0 <= nc < N:
                if rec[nr][nc] > rec[r][c] + arr[nr][nc]:
                    rec[nr][nc] = rec[r][c] + arr[nr][nc]
                    Q.append((nr,nc))
    return rec[N-1][N-1]


N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
rec = [[0xfffffff]*N for _ in range(N)]

print(BFS())