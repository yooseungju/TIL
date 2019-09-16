import sys
sys.stdin = open('input.txt')



def check(i,j):
    for x in range(i, i + 2):
        for y in range(j, j + 2):
            if not M[x][y]:
                return False
    return True

dy = (1,0,-1,0)
dx = (0,-1,0,1)

turn = {0:1,1:2,2:3,3:0}

N = int(input())
Size = 200

M = [[0]*Size for _ in range(Size)]
for _ in range(N):
    y, x, d, g = map(int, input().split())

    tmp = []
    tmp.append(d)
    M[x][y] = 1
    M[x+dx[d]][y+dy[d]] = 1
    x += dx[d]
    y += dy[d]

    for _ in range(g):
        # 그림 그리기
        length = len(tmp)
        for t in range(length-1, -1, -1):
            new_d = turn[tmp[t]]
            nx = x + dx[new_d]
            ny = y + dy[new_d]

            if 0<=nx<=100 and 0<=ny<=100:
                tmp.append(new_d)
                M[nx][ny]= 1
                x = nx
                y = ny

count = 0
for i in range(Size):
    for j in range(Size):
        if M[i][j] and check(i,j):
            count += 1

print(count)




