import sys
sys.stdin = open('input.txt')


def BFS():
    dj = [-1,1,0,0]
    di = [0,0,-1,1]

    Q = [(Rx,Ry,Bx,By,0)]

    rec[Rx][Ry][Bx][By] = 1


    while Q:
        rx, ry, bx, by, c = Q.pop(0)

        if c > 10:
            print(-1)
            return

        for m in range(4):
            nRx = rx + di[m]
            nRy = ry + dj[m]
            nBx = bx + di[m]
            nBy = by + dj[m]

            if 0 <= nRx < R and 0 <= nRy < C and 0 <= nBx < R and 0 <= nBy < C:

                if arr[nRx][nRy] == 'H':
                    print(c+1)
                    return
                if arr[nBx][nBy] == 'H':
                    continue
                if arr[nRx][nRy] != '#':
                    # 둘다 움직였을때
                    if arr[nBx][nBy] != '#' and not rec[nRx][nRy][nBx][nBy]:
                        rec[nRx][nRy][nBx][nBy] = 1
                        Q.append((nRx, nRy, nBx, nBy, c+1))

                    # 빨강만 움직였을때
                    elif arr[nBx][nBy] == '#' and not rec[nRx][nRy][bx][by]:
                        if nRx == bx and nRy ==  by:continue
                        rec[nRx][nRy][bx][by] = 1
                        Q.append((nRx, nRy, bx, by, c+1))

                # 파랑만 움직였을때
                elif arr[nBx][nBy] != '#' and not rec[rx][ry][nBx][nBy]:
                    if nBx == rx and nBy == ry:continue
                    rec[nRx][nRy][bx][by] =1
                    Q.append((rx, ry, nBx, nBy, c+1))

    print(-1)
    return


T  = int(input())
for _ in range(T):
    # 행 열
    R, C = map(int, input().split())
    arr = [list(input()) for _ in range(R)]

    rec = [[[[0]*C for _ in range(R)] for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'R':
                Rx = i
                Ry = j
            elif arr[i][j] == 'B':
                Bx = i
                By = j
            elif arr[i][j] == 'H':
                ex = i
                ey = j

    BFS()



