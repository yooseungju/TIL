import sys
sys.stdin = open('input.txt')

T = int(input())



def solution(i, j, flag, length):
    global M, K, N
    print(M[i][j])



    dj = [-1, 1, 0, 0]
    di = [0, 0, -1, 1]

    cnt = 0

    for d in range(4):
        if i + di[d] >= 0 and i+di[d] < N and j + dj[d] >= 0 and j+dj[d] < N:
            if M[i+di[d]][j+dj[d]] <  M[i][j]:
                solution(i+di[d], j+dj[d], flag, length+1)
            elif not flag:
                if M[i+di[d]][j+dj[d]] <  M[i][j] - K:
                    solution(i+di[d], j+dj[d], 1, length+1)
        else:
            cnt += 1
            if cnt == 4:
                return print(length)







for tc in range(T):
    N, K = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(N)]
    top = 0
    for i in range(N):
        for j in range(N):
            if M[i][j] >= top:
                top = M[i][j]

    top_list = [[i, j] for i in range(N) for j in range(N) if top == M[i][j]]

    # for t in top_list:
    #     solution(t[0],t[1], 0, 1)

    solution(0, 0, 0, 1)


