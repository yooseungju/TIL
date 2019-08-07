import sys
sys.stdin = open("input.txt")



dy = (-1,1,0,0)
dx = (0,0,-1,1)
block = {1: [2, 0, 3, 1], 2: [3, 0, 1, 2], 3: [1, 3, 0, 2], 4:[1,2,3,0],5: [1, 0, 3, 2]}


def BFS(i,j,d):
    global count
    M[i][j] = -1

    Q = [(i,j,d)]


    while len(Q)>0:
        x, y, d = Q.pop()
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0<= ny <N:
            nm = M[nx][ny]
            if nm == -1:
                return count

            elif nm in (1,2,3,4,5):
                Q.append((nx,ny,block[nm][d]))
                count+=1

            elif nm in (6,7,8,9,10):
                wh[nm]
                for i in range(2):
                    if wh[nm][i] != (nx,ny):
                        Q.append((wh[nm][i][0], wh[nm][i][1],d))
            else:
                Q.append((nx,ny,d))

        else:
            Q.append((nx, ny, block[5][d]))
            count += 1



T = int(input())


for tc in range(T):
    N=int(input())

    M = [list(map(int, input().split())) for _ in range(N)]

    wh = {6:[], 7:[], 8:[], 9:[], 10:[]}

    for i in range(N):
        for j in range(N):
            if M[i][j] in (6,7,8,9,10):
                wh[M[i][j]].append((i,j))

    MAX = 0
    for i in range(N):
        for j in range(N):
            if M[i][j] == 0:
                for d in range(4):
                    count = 0
                    BFS(i,j,d)
                    if count > MAX:
                        MAX = count
                M[i][j] = 0


    print(f"#{tc+1} {MAX}")

