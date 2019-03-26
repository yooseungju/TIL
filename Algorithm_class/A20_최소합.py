import sys
sys.stdin = open('A20_최소합_input.txt')


def DFS(s, e, SUM):
    global sum_min
    di = [1,0]
    dj = [0,1]
    if s == e:
        if sum_min > SUM:
            sum_min = SUM

    for m in range(2):
        if s[0] + di[m] < N and s[1] + dj[m] < N:
            if sum_min > SUM+M[s[0]+di[m]][s[1]+dj[m]]:
                DFS([s[0]+di[m], s[1]+dj[m]],e, SUM+M[s[0]+di[m]][s[1]+dj[m]])


T = int(input())
for tc in range(T):
    N = int(input())

    M = [list(map(int, input().split())) for _ in range(N)]
    visited=[[0 for _ in range(N)] for _ in range(N)]
    A = [i for i in range(N)]
    sum_min = 0x7fffffff

    DFS([0,0], [N-1,N-1], M[0][0])
    print('#{} {}'.format(tc+1, sum_min))