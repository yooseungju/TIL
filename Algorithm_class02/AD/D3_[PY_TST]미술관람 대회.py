import sys
sys.stdin = open('input.txt')




def BFS(i, j, char, M, flag):
    dj = [-1, 1, 0,0]
    di = [0,0,-1,1]
    Q = [[i,j]]
    M[i][j] = 0
    while len(Q) > 0:
        q = Q.pop(0)
        for m in range(4):
            if q[0] + di[m] >= 0 and q[1] + dj[m] >= 0 and q[0] + di[m] < N and q[1] + dj[m] < N:
                if not flag:
                    if M[q[0]+di[m]][q[1]+dj[m]] == char:
                        M[q[0] + di[m]][q[1] + dj[m]] = 0
                        Q.append([q[0] + di[m], q[1] + dj[m]])
                else:
                    if char != 'B':
                        if M[q[0]+di[m]][q[1]+dj[m]] != 'B' and M[q[0]+di[m]][q[1]+dj[m]] != 0:
                            M[q[0] + di[m]][q[1] + dj[m]] = 0
                            Q.append([q[0] + di[m], q[1] + dj[m]])

                    elif char == 'B' and M[q[0]+di[m]][q[1]+dj[m]] == char:
                        M[q[0] + di[m]][q[1] + dj[m]] = 0
                        Q.append([q[0] + di[m], q[1] + dj[m]])

N = int(input())
M = [list(input()) for _ in range(N)]
cnt = 0
GGcnt = 0
tm = [M[m][:] for m in range(N)]



for i in range(N):
    for j in range(N):
        if M[i][j] != 0:
            cnt+=1
            BFS(i, j, M[i][j], M, 0)
print(cnt , end = ' ')

for i in range(N):
    for j in range(N):
        if tm[i][j] != 0:
            GGcnt+=1
            BFS(i, j, tm[i][j], tm, 1)

print(GGcnt)





