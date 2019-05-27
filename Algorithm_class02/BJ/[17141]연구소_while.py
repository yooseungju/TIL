import sys
sys.stdin = open('input.txt')

N,M = map(int, input().split())

Origin = [list(map(int, input().split())) for _ in range(N)]
dj = (-1,1,0,0)
di = (0,0,-1,1)


def sol(tmp):

    flag = True

    G = [[0] * N for _ in range(N)]

    for b in tmp:
        x = b_list[b][0]
        y = b_list[b][1]
        G[x][y] = 2

    cnt = 0

    while flag:
        visited = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if G[i][j] == 0 and Origin[i][j] != 1:
                    for m in range(4):
                        nx = i + di[m]
                        ny = j + dj[m]
                        if 0<=nx<N and 0<=ny<N and G[nx][ny] == 2:
                            visited[i][j] = 2
                            flag = False
                            break


        if not flag:
            cnt += 1
            flag = True
            for i in range(N):
                for j in range(N):
                    if visited[i][j] == 2:
                        G[i][j] = 2


        else:
            for i in range(N):
                for j in range(N):
                    if G[i][j] == 0 and Origin[i][j] == 0:
                        return False
            return cnt



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



b_list = []
tmp = []
Min = 0xfffffff

for i in range(N):
    for j in range(N):
        if Origin[i][j] == 2:
            b_list.append((i, j))


com(0,len(b_list),tmp)


if Min == 0xfffffff:
    print(-1)
else:
    print(Min)