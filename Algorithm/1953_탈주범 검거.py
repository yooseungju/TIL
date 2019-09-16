import sys
sys.stdin = open('input.txt')


# dx dy


pip = {1:((-1,1,0,0),(0,0,-1,1)), #상하좌우
       2:((-1,1),(0,0)), # 상하
       3:((0,0),(-1,1)), # 좌우
       4:((-1,0),(0,1)), # 상우
       5:((1,0),(0,1)),  # 하우
       6:((1,0),(0,-1)), # 하좌
       7:((-1,0),(0,-1))} # 상좌

link = {1:((3,4,7),(3,5,6),(2,6,7),(2,4,5)),
        2:((3,4,7),(3,5,6)),
        3:((2,6,7),(2,4,5)),
        4:((3,4,7),(2,4,5)),
        5:((3,5,6),(2,4,5)),
        6:((3,5,6),(2,6,7)),
        7:((3,4,7),(2,6,7))}

def BFS(q):
    new_q = []

    while len(q):
        x,y = q.pop(0)
        d = M[x][y]

        pip_len = len(pip[d][0])

        for m in range(pip_len):
            nx = x + pip[d][0][m]
            ny = y + pip[d][1][m]

            if 0<=nx<r and 0<= ny < c and not visited[nx][ny] and M[nx][ny] and not M[nx][ny] in link[d][m]:
                visited[nx][ny] = 1
                new_q.append((nx,ny))

    return new_q



T = int(input())
for tc in range(T):
    r, c, x, y, time = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(r)]
    visited = [[0]*c for _ in range(r)]

    q = [(x,y)]
    visited[x][y] = 1
    count = 1

    for _ in range(time-1):

        q = BFS(q)
        count += len(q)

    print("#{} {}".format(tc+1, count))
