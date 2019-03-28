import sys
sys.stdin = open('input.txt')


def BFS(i,j):
    global M
    dj = [-1,1,0,0]
    di = [0,0,-1,1]
    M[i][j] = cnt
    Q = []
    Q.append([i,j])

    C = 1
    while len(Q) > 0:
        q = Q.pop(0)
        for m in range(4):
            if q[0] +di[m] >= 0 and q[0]+di[m] < N and q[1]+ dj[m] >= 0 and q[1]+ dj[m]<N and M[q[0]+di[m]][q[1]+dj[m]] == '1':
                C += 1
                M[q[0] + di[m]][q[1] + dj[m]] = cnt
                Q.append([q[0] + di[m], q[1] + dj[m]])

    return C

N = int(input())
M = [list(input()) for _ in range(N)]
cnt = 0
tmp = []
for i in range(N):
    for j in range(N):
        if M[i][j] == '1':
            cnt+=1
            tmp.append(BFS(i,j))


print(cnt)
tmp.sort()
for t in tmp:
    print(t)

