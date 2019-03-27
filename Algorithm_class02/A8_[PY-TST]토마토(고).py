import sys
sys.stdin = open('input.txt')






def BFS():
    global Max
    Q = tomato

    dj = [-1,1,0,0]
    di = [0,0,-1,1]

    while len(Q)>0:
        q = Q.pop(0)
        cnt = 0
        for m in range(4):
            if q[0] + di[m] >= 0 and q[0] + di[m] < Y and q[1] + dj[m] >= 0 and q[1] + dj[m] < X and M[q[0] + di[m]][q[1] + dj[m]] == 0:
                M[q[0] + di[m]][q[1] + dj[m]] = M[q[0]][q[1]] + 1
                Q.append([q[0] + di[m],q[1] + dj[m]])
            else:cnt+=1



        if cnt == 4:
            if Max < M[q[0]][q[1]]-1:
                Max = M[q[0]][q[1]]-1



X, Y = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(Y)]
Max = 0

tomato =  [[i,j] for i in range(Y) for j in range(X) if M[i][j] == 1]
BFS()
flag = True
for i in range(Y):
    for j in range(X):
        if M[i][j] == 0:
            flag = False
            break
if flag:
    print(Max)
else:
    print(-1)