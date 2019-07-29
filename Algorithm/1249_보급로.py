import sys
sys.stdin = open("input.txt")

T = int(input())




dy = (-1,1,0,0)
dx = (0,0,-1,1)

def BFS():
    Q = [(0,0)]
    global Min

    for i in range(4):
        visited[0][0] = M[0][0]


    while len(Q) > 0:
        x, y = Q.pop()

        r = 0
        c = 0
        tmpMin = 0xfffffff

        for m in range(4):

            nx = x + dx[m]
            ny = y + dy[m]

            if 0 <= nx < N and 0 <= ny < N:


                if nx == N-1 and ny == N-1:
                    if visited[x][y] + M[nx][ny] < Min:
                        Min = visited[x][y] + M[nx][ny]


                elif visited[nx][ny] == 0xfffffff:
                    if M[nx][ny] <= tmpMin:
                        r = nx
                        c = ny
                        tmpMin = visited[x][y] + M[nx][ny]


        visited[r][c] = tmpMin
        Q.append((r,c))


for tc in range(T):
    N = int(input())
    M = [list(map(int, list(input()))) for _ in range(N)]
    Min = 0xfffffff

    visited =  [[0xfffffff for _ in range(N)] for _ in range(N)]
    BFS()
    print(f"#{tc+1} {Min}")