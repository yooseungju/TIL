import sys

sys.stdin  = open('input.txt')

import copy


def BFS(i, j, g):

    dj = [-1,1,0,0]
    di = [0,0,-1,1]

    Q = [[i,j]]

    g[i][j] = 2


    while len(Q) > 0:
        q = Q.pop(0)
        if g[q[0]][q[1]]-1 > MIN:
            return
        if q[0] == N-1 and q[1] == M-1:
            return g[q[0]][q[1]]-1

        for m in range(4):
            if q[0]  + di[m] >= 0 and q[1] + dj[m] >=0 and q[0]  + di[m] < N and q[1] + dj[m] < M:
                if g[q[0]  + di[m]][q[1] + dj[m]] == 0:
                    g[q[0] + di[m]][q[1] + dj[m]] = g[q[0]][q[1]] + 1
                    Q.append([q[0] + di[m],q[1] + dj[m]])
    return

N, M = map(int , input().split())
G = [list(map(int,list(input()))) for _ in range(N)]


MIN =  0xfffffff
for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            G[i][j] = 0
            tmp = [g[::] for g in G]
            ans = BFS(0,0,tmp)
            if ans != None:
                if ans < MIN:
                    MIN = ans
            G[i][j] = 1


if MIN == 0xfffffff:
    print(-1)
else:
    print(MIN)