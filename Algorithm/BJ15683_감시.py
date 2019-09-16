import sys
sys.stdin = open('input.txt')




dy = (1,0,-1,0)
dx = (0,-1,0,1)

turn = (0,
        0,
        {0:(0,2),1:(1,3)},
        {0:(0,1),1:(1,2),2:(2,3),3:(3,0)},
        {0:(0,1,2),1:(1,2,3),2:(2,3,0),3:(3,0,1)})


def change(tmp_M,d,i,j):
    Q = [(i,j)]

    while Q:
        x,y = Q.pop(0)
        nx = x + dx[d]
        ny = y + dy[d]

        if 0<=nx<r and 0<=ny<c and tmp_M[nx][ny] != 6:
            tmp_M[nx][ny] = '#'
            Q.append((nx,ny))


def check():
    global MIN
    tmp_M = [M[i][::] for i in range(r)]

    for i in range(length):
        if CCTV[i][2] == 1:
            change(tmp_M,CCTV_trun[i],CCTV[i][0],CCTV[i][1])

        elif CCTV[i][2] == 5:
            for m in range(4):
                change(tmp_M,m,CCTV[i][0],CCTV[i][1])

        else:


            for d in turn[CCTV[i][2]][CCTV_trun[i]]:
                change(tmp_M,d,CCTV[i][0],CCTV[i][1])


    count =  0

    for i in range(r):
        for j in range(c):
            if tmp_M[i][j] == 0:
                count+= 1

    if count < MIN:
        MIN = count

def dfs(n):
    if n == length:
        check()
        return

    if CCTV[n][2] == 5:
        dfs(n+1)

    elif CCTV[n][2] == 2:
        for i in range(2):
            CCTV_trun[n] = i
            dfs(n+1)
            CCTV_trun[n] = 0

    else:
        for i in range(4):
            CCTV_trun[n] = i
            dfs(n+1)
            CCTV_trun[n] = 0


r, c = map(int, input().split())
M = [list(map(int,input().split())) for _ in range(r)]

CCTV = []

for i in range(r):
    for j in range(c):
        if M[i][j] and M[i][j] != 6:
            CCTV.append((i,j,M[i][j]))

MIN = 0xfffffff
length = len(CCTV)
CCTV_trun = [0]*length
dfs(0)
print(MIN)