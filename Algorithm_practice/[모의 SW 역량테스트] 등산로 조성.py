import copy
import sys
sys.stdin = open('input.txt')



def solution_dfs(i, j, flag, cnt ,M):
    #flag 산을 깎았는지 안깍았는지

    global N, K, Max_length
    dj = [-1, 1, 0, 0]
    di = [0, 0, -1, 1]
    c = 0
    for m in range(4):
        if i + di[m] >= 0 and i + di[m] < N and j + dj[m] >= 0 and  j + dj[m] < N:
            tmp_M = copy.deepcopy(M)
            if M[i+di[m]][j+dj[m]] < M[i][j]:
                tmp_M[i][j] = 100
                solution_dfs(i + di[m], j + dj[m], flag, cnt+1, tmp_M)
            elif flag == 0:
                for k in range(1,K+1):
                    if M[i+di[m]][j+dj[m]] - k < M[i][j]:
                        tmp_M[i][j] = 100
                        tmp_M[i + di[m]][j + dj[m]] -= k
                        solution_dfs(i + di[m], j + dj[m], 1, cnt+1, tmp_M)

    if cnt > Max_length:
        Max_length = cnt


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(N)]

    Max = 0
    for i in range(N):
        for j in range(N):
            if M[i][j] > Max:
                Max = M[i][j]

    height = [[i,j]for i in range(N) for j in range(N) if M[i][j] ==  Max]

    Max_length = 0
    for h in height:
        solution_dfs(h[0],h[1], 0, 1, M)
    print('#{} {}'.format(tc+1, Max_length))