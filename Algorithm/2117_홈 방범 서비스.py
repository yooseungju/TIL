import sys
sys.stdin = open('input.txt')

T = int(input())

dy = (-1,1,0,0)
dx = (0,0,-1,1)


def expend(i,j):
    K = 0

    K = N*2

    q = [(i,j)]
    visited[i][j] = 1

    if D[i][j]:
        count = 1
    else:
        count = 0

    while len(q)>0:
        x,y = q.pop(0)
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                if D[nx][ny]:
                    count += 1
                    KL[visited[nx][ny]] = count

                if visited[nx][ny] == K:
                    return


for tc in range(T):
    N, M = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(N)]
    Max = 0

    for i in range(N):
        for j in range(N):

            KL = {x: 0 for x in range(1, (N-1*2)-1)}
            KL[1] += 1
            visited = [[0]*N for _ in range(N)]
            expend(i,j)

            for k , v in KL.items():
                if v and (k*k)+((k-1)*(k-1)) <= v*M and v > Max:
                    Max = v

    print("#{} {}".format(tc+1, Max))

#-----------------------------------------------------------------
# def get_service_cost(K):
#     return (K + 1) * (K + 1) + K * K
#
# for test_case in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#     maxCount = 0
#     maxK = 2 * N - 1
#     for r in range(N):
#         for c in range(N):
#             counts = [0] * maxK
#             for r1 in range(N):
#                 for c1 in range(N):
#                     if grid[r1][c1] > 0:
#                         counts[abs(r - r1) + abs(c - c1)] += 1
#             countsSum = sum(counts)
#             for k in range(maxK - 1, -1, -1):
#                 if countsSum * M >= get_service_cost(k):
#                     maxCount = max(maxCount, countsSum)
#                     break
#                 countsSum -= counts[k]
#     print("#{} {}".format(test_case, maxCount))


