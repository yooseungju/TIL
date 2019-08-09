import sys
sys.stdin = open("input.txt")

T = int(input())


dx = (-1,1,0,0)
dy = (0,0,-1,1)

crush = {0:1, 1:0, 2:3, 3:2}

def BFS(q):
    global count
    new = {}
    new_q = []
    while len(q)>0:

        x,y,d,k  =  q.pop(0)

        nx = x + dx[d]
        ny = y + dy[d]

        if rx<=nx<=hx and ry<=ny<=hy:
            #origin 없고
            if not M[nx][ny]:
                # 동시에 같은 자리에 경우도 없으면

                if (nx,ny) not in new.keys():
                    new[(nx,ny)]=[d,k]

                # 동시에 같은 자리에 가는 경우가 있으면
                else:
                    print("d")
                    new[(nx,ny)].append(k)


            else:
                count += (M[x][y] + M[nx][ny])
                M[x][y] = 0
                M[nx][ny] = 0

        M[x][y] = 0
    for k,v in new.items():
        x, y = k

        if len(v) > 2:
            count += sum[v[1:]]
        else:
            new_q.append((x,y,v[0],v[1]))

    return new_q




for _ in range(T):
    N = int(input())
    M = [[0]*3000 for _ in range(3000)]

    Q = []

    count = 0

    rx = 0xfffffff
    hx = 0

    ry = 0xfffffff
    hy = 0



    for _ in range(N):
        i, j, d, k  =  map(int, input().split())
        i += 1000
        j += 1000

        if i < rx:
            rx =i
        if i > hx:
            hx = i
        if j < ry:
            ry = j
        if j > hy:
            hy = j

        Q.append((i,j,d,k))
        M[i][j] = k


    print(rx,hx,ry,hy)


    while len(Q) > 0:
        Q = BFS(Q)


    print(count)


