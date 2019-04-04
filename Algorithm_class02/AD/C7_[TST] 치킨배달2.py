import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())



def DFS(k, n):
    global  MIN, tmp, MIN_SUM
    if len(tmp) > M: return

    if k == n:
        SUM = 0
        for i in range(len(H)):
            MIN  =  0xfffffff
            for j in range(len(C)):
                if j in tmp:
                    if G[i][j] < MIN:
                        MIN = G[i][j]
            SUM += MIN
        if SUM < MIN_SUM:
            MIN_SUM = SUM


        if SUM < MIN:
            MIN = SUM
        return
    else:
        tmp.append(k)
        DFS(k+1, n)
        tmp.pop()
        DFS(k+1, n)

city = [input().split() for _ in range(N)]

C = []
H = []
tmp = []
for i in range(N):
    for j in range(N):
        if city[i][j] == '1':
            H.append([i,j])
        elif city[i][j] == '2':
            C.append([i,j])


G = [[0] * len(C) for _ in range(len(H))]

# 홈에서 치킨집으로 가는 거리
for h in range(len(H)):
    for c in range(len(C)):
        G[h][c] = abs(H[h][0] - C[c][0]) + abs(H[h][1] - C[c][1])



MIN_SUM = 0xfffffff
DFS(0,len(C))

print(MIN_SUM)