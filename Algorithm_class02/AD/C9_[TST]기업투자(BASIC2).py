import sys
sys.stdin = open('input.txt')


def DFS(k, start):
    global MAX
    if sum(tmp) > M:
        return

    if k == M:
        print(tmp)
        # if sum(tmp) < M:
        #     print(tmp)
        #     GG = [g[::] for g in G]
        #     SUM = 0
        #
        #     for i in range(N):
        #
        #         m = max(GG[tmp[i]-1][1:N+1])
        #         SUM += m
        #         GG[tmp[i]-1][GG[tmp[i]-1].index(m)] = 0
        #
        #     if SUM > MAX:
        #         MAX = SUM
        #     # [1,3], [2,2]
        # tmp[k - 1] = 0
        # return


    tmp[k] = i
    DFS(k+1, i)

M, N = map(int, input().split())
G = [list(map(int,input().split())) for _ in range(M)]
tmp = []
MAX = max(G[M-1][1:N+1])
DFS(0,1)
print(MAX)


