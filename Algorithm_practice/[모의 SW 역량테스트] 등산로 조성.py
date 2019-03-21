import sys
sys.stdin = open('input.txt')



def solution_dfs(i,j,flag):
    #flag 산을 깎았는지 안깍았는지

    global M, N, K
    dj = [-1, 1, 0, 0]
    di = [0, 0, -1, 1]
    cnt = 0
    flag = 0
    Stack = []

    Stack.append([i,j])

    cut = []
    while len(Stack) > 0:
        s = Stack.pop(-1)
        for m in range(4):
            if s[0] + di[m] >= 0 and s[0] + di[m] < N and s[1] + dj[m] >= 0 and  s[1] + dj[m] < N:
                if M[s[0]+di[m]][s[1]+dj[m]] < M[s[0]][s[1]]:
                    Stack.append(M[s[0]+di[m]][s[1]+dj[m]])
                    cnt += 1

                elif flag == 0 and M[s[0]+di[m]][s[1]+dj[m]] - K < M[s[0]][s[1]]:
                    Stack.append(M[s[0] + di[m]][s[1] + dj[m]])
                    M[s[0] + di[m]][s[1] + dj[m]] -= K
                    cut = [s[0] + di[m], s[1] + dj[m]]
                    flag = 1
            if len(cut) > 0 and [s[0] , s[1]]  == cut[-1]:
                M[s[0]][s[1]] += K
                cut.pop()










T = int(input())
for tc in range(T):
    N , K = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(N)]

    Max = 0
    for i in range(N):
        for j in range(N):
            if M[i][j] > Max:
                Max = M[i][j]
    height = [[i,j]for i in range(N) for j in range(N) if M[i][j] ==  Max]


    for h in height:
        solution_dfs(h, flag)


    print('#{} {}'.format(tc+1, solution()))