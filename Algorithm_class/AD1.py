import sys
sys.stdin = open('input.txt')
import time


def isWall(x, y):
    if x < 0 or x > N-1 or y < 0 or y > N-1:
        return True
    else: return False


def dfs(i, j, pre_m):
    global N, M, cnt
    global flag


# 우 우하 하 우하
    di = [0, 1, 1]
    dj = [1, 1, 0]

    if i == N-1 and j == N-1 and (pre_m == 0 or pre_m == 2):
        cnt += 1

    elif not flag:
        flag = 1
        for m in [0, 2]:
            if not isWall(i + di[m], j + dj[m]) and M[i + di[m]][j + dj[m]] == 0:
                dfs(i + di[m], j + dj[m], m)

    else:
        if pre_m == 0:
            for m in range(0,2):
                if not isWall(i + di[m], j + dj[m]) and M[i + di[m]][j + dj[m]] == 0:
                    if m == 1:
                        if M[i + di[0]][j + dj[0]] == 0 and M[i + di[2]][j + dj[2]] == 0:
                            dfs(i + di[m], j + dj[m], m)
                    else:
                        dfs(i + di[m], j + dj[m], m)

        elif pre_m == 1:
            for m in range(3):
                if not isWall(i + di[m], j + dj[m]) and M[i + di[m]][j + dj[m]] == 0:
                    if m == 1:
                        if M[i + di[0]][j + dj[0]] == 0 and M[i + di[2]][j + dj[2]] == 0:
                            dfs(i + di[m], j + dj[m], m)
                    else:
                        dfs(i + di[m], j + dj[m], m)


        elif pre_m == 2:
            for m in range(2, 0,-1):
                if not isWall(i + di[m], j + dj[m]) and M[i + di[m]][j + dj[m]] == 0:
                    if m == 1:
                        if M[i + di[0]][j + dj[0]] == 0 and M[i + di[2]][j + dj[2]] == 0:
                            dfs(i + di[m], j + dj[m], m)
                    else:
                        dfs(i + di[m], j + dj[m], m)


T = int(input())
for tc in range(T):
    start_time = time.time()
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    flag = 0
    dfs(0, 0, 0)
    print('#{} {}'.format(tc+1,cnt))
    print("--- %s seconds ---" %(time.time() - start_time))