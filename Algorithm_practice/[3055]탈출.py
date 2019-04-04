import sys
sys.stdin = open('input.txt')



def BFS(Q):
    dj = [-1,1,0,0]
    di = [0,0,-1,1]

    while Q:
        x, y, a = Q.pop(0)
        if a != 'W':
            if x == D[0] and y == D[1]:
                return a
        for m in range(4):
            nx = x + di[m]
            ny = y + dj[m]
            if 0<= nx < R and 0 <= ny <C and M[nx][ny] != 'X':
                if a == 'W':
                    if  M[nx][ny] != 'D' and  V[nx][ny] != '*':
                        V[nx][ny] = '*'
                        Q.append([nx, ny,'W'])
                else:
                    if M[nx][ny] == 'D':
                        return (a+1)
                    elif M[nx][ny] == '.' and V[nx][ny] == -1:
                        V[nx][ny] = 0
                        Q.append([nx, ny, a+1])




# main -----------------------------------------------------------------

R, C = map(int, input().split())
M = [list(input()) for _ in range(R)]
V = [[-1]*C for _ in range(R)]
startQ = []
D = ''
S = ''

for i in range(R):
    for j in range(C):
        if M[i][j] == '*':
            V[i][j] = '*'
            startQ.append([i,j,'W'])
        elif M[i][j] == 'D':
            D = [i, j]
        elif M[i][j] == 'S':
            V[i][j] = 0
            S = [i,j,0]
startQ.append(S)
ANS =  BFS(startQ)

if ANS == None:
    print('KAKTUS')
else:
    print(ANS)


