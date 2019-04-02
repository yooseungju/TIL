import sys
sys.stdin = open('input.txt')



def BFS(i,j,d):
    dj = [-1,1,0,0]
    di = [0,0,-1,1]

    Q = [[i,j,d]]

    while len(Q) > 0:
        q = Q.pop(0)

        for m in pip[q[2]]:
            if q[0]+di[m] >= 0 and q[1]+dj[m] >= 0 and  q[0]+di[m] < N and q[1]+dj[m] < N and M[q[0] + di[m]][q[1] + dj[m]] != '0' and M[q[0] + di[m]][q[1] + dj[m]] != 0:
                if m == 0:
                    if 1 in pip[M[q[0] + di[m]][q[1] + dj[m]]]:
                        Q.append([q[0] + di[m], q[1] + dj[m],M[q[0] + di[m]][q[1] + dj[m]]])
                        M[q[0] + di[m]][q[1] + dj[m]] = 0
                elif m == 1:
                    if 0 in pip[M[q[0] + di[m]][q[1] + dj[m]]]:
                        Q.append([q[0] + di[m], q[1] + dj[m],M[q[0] + di[m]][q[1] + dj[m]]])
                        M[q[0] + di[m]][q[1] + dj[m]] = 0

                elif m == 2:
                    if 3 in pip[M[q[0] + di[m]][q[1] + dj[m]]]:
                        Q.append([q[0] + di[m], q[1] + dj[m],M[q[0] + di[m]][q[1] + dj[m]]])
                        M[q[0] + di[m]][q[1] + dj[m]] = 0

                elif m == 3:
                    if 2 in pip[M[q[0] + di[m]][q[1] + dj[m]]]:
                        Q.append([q[0] + di[m], q[1] + dj[m],M[q[0] + di[m]][q[1] + dj[m]]])
                        M[q[0] + di[m]][q[1] + dj[m]] = 0




# 좌우상하 0 1,2,3
pip = {'1':[0,1] , '2':[2,3], '3':[1,3], '4':[0,3], '5':[0,2], '6':[1,2],'7':[1,2,3], '8':[0,1,3], '9':[0,2,3], 'A':[0,1,2],'B':[0,1,2,3]}

N = int(input())
x,y = map(int, input().split())
M = [list(input()) for _ in range(N)]
BFS(y,x,M[y][x])

cnt = 0
for i in range(N):
    for j in range(N):
        if not(M[i][j]  == 0 or M[i][j] =='0'):
            cnt +=1

print(cnt)