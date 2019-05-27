import sys
sys.stdin = open('input.txt')


def sol(tmp):
    zero_cnt = 0
    G = [[0]*N for _ in range(N)]
    Q = [b_list[i] for i in tmp]
    Max = 0
    for b in tmp:
        x = b_list[b][0]
        y = b_list[b][1]
        G[x][y] = 1

    while len(Q) > 0:
        i,j  = Q.pop(0)
        for m in range(4):
            nx = i + di[m]
            ny = j + dj[m]

            if 0<=nx<N and 0<=ny<N and G[nx][ny] == 0 and Origin[nx][ny] != 1:
                G[nx][ny] = G[i][j] + 1

                if G[nx][ny] > Max:
                    Max = G[nx][ny]


                Q.append((nx, ny))

    if zero_cnt == zero:
            return False
    return Max-1




def com(k, n, tmp):
    global Min

    if k == n:
        if len(tmp) == M:
            result = sol(tmp)
            if result:
                if result < Min:
                    Min = result
        return

    else:
        tmp.append(k)
        com(k + 1, n, tmp)
        tmp.pop()
        com(k+1, n, tmp)

#--------------------------------main---------------------------------------
N,M = map(int, input().split())

Origin = [list(map(int, input().split())) for _ in range(N)]
dj = (-1,1,0,0)
di = (0,0,-1,1)

b_list = []
wall_list = []
Min = 0xfffffff
zero = 0

for i in range(N):
    for j in range(N):
        if Origin[i][j] == 2:
            b_list.append((i, j))
        elif Origin[i][j] == 0:
            zero += 1


tmp = []

com(0,len(b_list),tmp)

if Min != 0xfffffff:
    print(Min)
else:
    print(-1)