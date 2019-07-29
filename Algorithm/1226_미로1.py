import sys
sys.stdin = open("input.txt")




def BFS(i,j):
    global ans

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    Q =[(i,j)]
    M[i][j] = 1

    while len(Q) > 0:
        x,y = Q.pop()

        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]

            if M[nx][ny] == 3:
                return 1

            if M[nx][ny] == 0:
                Q.append((nx,ny))
                M[nx][ny] = 1

    return 0

def getStart():
    for i in range(16):
        for j in range(16):
            if M[i][j] == 2:
                print(f"#{tc+1} {BFS(i, j)}")


for tc in range(10):
    t = input()
    M = [list(map(int, list(input())))for _ in range(16)]
    ans = 0
    getStart()
    # print(f"#{tc+1} {ans}")