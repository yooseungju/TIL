import sys
import copy
sys.stdin = open('input.txt')

T = int(input())



<<<<<<< HEAD
def solution(i, j, flag, length, M):
    global K, N, Max
    print(i,j , M[i][j], 'length', length)
=======
def solution(i, j, flag, length):
    global M, K, N
    print(M[i][j])

>>>>>>> 3de8ff03c7463c2f36c0c0a620cb27c7daa480f0

    dj = [-1, 1, 0, 0]
    di = [0, 0, -1, 1]


    cnt = 0

    for d in range(4):
        if i + di[d] >= 0 and i+di[d] < N and j + dj[d] >= 0 and j+dj[d] < N:
            if M[i+di[d]][j+dj[d]] <  M[i][j]:
<<<<<<< HEAD
                solution(i+di[d], j+dj[d], flag, length+1,M)
=======
                solution(i+di[d], j+dj[d], flag, length+1)

>>>>>>> 3de8ff03c7463c2f36c0c0a620cb27c7daa480f0
            elif not flag:
                if M[i+di[d]][j+dj[d]] - K <  M[i][j]:
                    tmp_M = copy.deepcopy(M)
                    tmp_M[i+di[d]][j+dj[d]] = M[i+di[d]][j+dj[d]] - K
                    solution(i+di[d], j+dj[d], 1, length+1, tmp_M)
                else: cnt += 1
            else:
                cnt += 1

<<<<<<< HEAD

    if cnt == 3:
        if Max < length:
            Max = length
        return





=======
>>>>>>> 3de8ff03c7463c2f36c0c0a620cb27c7daa480f0
for tc in range(T):

    N, K = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(N)]
    top = 0
    for i in range(N):
        for j in range(N):
            if M[i][j] >= top:
                top = M[i][j]

    top_list = [[i, j] for i in range(N) for j in range(N) if top == M[i][j]]
<<<<<<< HEAD

    Max = 0

    for t in top_list:
        solution(t[0],t[1], 0, 1, M)
        print('------------------------')
=======
    # for t in top_list:
    #     solution(t[0],t[1], 0, 1)
>>>>>>> 3de8ff03c7463c2f36c0c0a620cb27c7daa480f0

    print('#{} {}'.format(tc+1, Max))


