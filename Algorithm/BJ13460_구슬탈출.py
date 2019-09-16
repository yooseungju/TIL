import sys
sys.stdin = open('input.txt')



dy = (-1,1,0,0)
dx = (0,0,-1,1)

def BFS(q):

    while q:
        rx, ry, bx, by = q.pop(0)
        print(rx,ry,bx,by, visited[rx][ry][bx][by])
        if visited[rx][ry][bx][by] == 11:
            print(-1)
            return

        for m in range(4):
            nrx = rx + dx[m]
            nry = ry + dy[m]
            nbx = bx + dx[m]
            nby = by + dy[m]

            if 0<=nrx<N and 0<=nry<M  and board[nrx][nry] != "#":
                if board[nrx][nry] == 'O':
                    print(visited[rx][ry][bx][by])
                    return
            else:
                nrx = rx
                nry = ry

            if 0<=nbx<M and 0<=nby<M and board[nbx][nby] != "#":
                if board[nbx][nby] == "O":
                    continue
            else:
                nbx = bx
                nby = by

            if (nrx,nry) != (nbx,nby) and not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = visited[rx][ry][bx][by] + 1
                q.append(((nrx,nry,nbx,nby)))


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
for i in range(N):

    for j in range(M):
        if board[i][j] == 'R':
            rx,ry = (i,j)
        elif board[i][j] == 'B':
            bx,by = (i,j)


visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

MIN = 0xfffffff

Q = [(rx,ry,bx,by)]

visited[rx][ry][bx][by] = 1
BFS(Q)



