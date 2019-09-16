import sys
sys.stdin = open('input.txt')


T = int(input())


dy = (0,0,0,-1,1)
dx = (0,-1,1,0,0)

cd = {1:2,2:1,3:4,4:3}

def BFS(q):
    global cnt
    visited = [ [0]*N for _ in range(N)]

    while q:
        x, y, num, m = q.pop(0)

        nx = x + dx[m]
        ny = y + dy[m]


        if 0<=nx<N and 0<=ny<N:
            if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
                num = num//2
                m = cd[m]

            # visited = [미생물 수, 방향, 가장큰 미생물 수]

            if visited[nx][ny]:
                if visited[nx][ny][2] < num:
                    visited[nx][ny][0] += num
                    visited[nx][ny][1] = m
                    visited[nx][ny][2] = num
                else:
                    visited[nx][ny][0] += num

            else:
                visited[nx][ny] = [num, m, num]

    tmp = []
    t_cnt = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                tmp.append((i,j,visited[i][j][0],visited[i][j][1]))
                t_cnt += visited[i][j][0]

    return tmp, t_cnt



for tc in range(T):
    #셀 , 시간, 군집 수
    N, M, K = map(int, input().split())

    q = []

    for _ in range(K):
        i,j,n,d = map(int, input().split())
        q.append((i,j,n,d))



    ans = 0
    for _ in range(M):
        q , ans= BFS(q)


    print('#{} {}'.format(tc+1, ans))









