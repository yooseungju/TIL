
import sys
sys.stdin = open("input.txt")

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

def BFS(q):
    new_q = []
    while len(q)>0:
        x,y = q.pop(0)

        o = matrix[x][y][0]
        z = matrix[x][y][1]


        #확장
        if z <= 0:
            for m in range(4):
                nx = x + dx[m]
                ny = y + dy[m]

                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = [o,o]
                    new_q.append((nx,ny))



                #동시에 같은 곳
                elif matrix[nx][ny] != "false" and matrix[nx][ny][0] == matrix[nx][ny][1] and (nx,ny) in new_q:
                    if matrix[nx][ny][0] < o:
                        matrix[nx][ny] = [o,o]

        #시간 지나기
        matrix[x][y][1] -= 1

        #세포 죽이기
        if matrix[x][y][1] != -o:
            new_q.append((x,y))
        else:
            matrix[x][y] = "false"
    return new_q


T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())

    D = [list(map(int, input().split())) for _ in range(N)]
    matrix = [[0]*1001 for _ in range(1001)]

    Q =[]

    for i in range(N):
        for j in range(M):
            if D[i][j]:
                matrix[500+i][500+j] = [D[i][j], D[i][j]]
                Q.append((500+i, 500+j))


    while K > 0:
        Q = BFS(Q)
        K -= 1



    print(f"#{tc+1} {len(Q)}")