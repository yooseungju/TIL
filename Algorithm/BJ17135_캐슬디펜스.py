import sys
sys.stdin = open('input.txt')


dy = (-1,0,1)
dx = (0,-1,0)
def search(tmp_M):
    cnt = 0
    shuter = [[], [], []]

    visited = [[[0]*3 for _ in range(c)] for _ in range(r+1)]

    Q = []

    for i in range(3):
        Q.append((r,tmp[i],i))

    while Q:
        x, y, shuter_idx = Q.pop(0)

        for m in range(3):
            nx = x + dx[m]
            ny = y + dy[m]

            if 0 <= nx < r and 0 <= ny < c and abs(nx-r) + abs(ny-tmp[shuter_idx]) <= D and not visited[nx][ny][shuter_idx]:
                if tmp_M[nx][ny]:
                    if not shuter[shuter_idx]:
                        shuter[shuter_idx]=(nx,ny,visited[x][y][shuter_idx]+1)
                    else:
                        break

                Q.append((nx,ny,shuter_idx))
                visited[nx][ny][shuter_idx] = (visited[x][y][shuter_idx] + 1)


    for i in range(3):
        if shuter[i]:
            x, y, o = shuter[i]
            if tmp_M[x][y]:
                tmp_M[x][y] = 0
                cnt += 1
    return cnt

def down():
    global MAX
    tmp_M = [map[i][:] for i in range(r)]
    count = 0

    for _ in range(r):
        count += search(tmp_M)
        tmp_M.pop()
        tmp_M.insert(0,[0]*c)


    if count > MAX:
        MAX = count


def com(n, s):
    if n == 3:
        down()
        return

    for i in range(s, c):
        tmp[n] = i
        com(n+1,i+1)
        tmp[n] = 0

r, c, D = map(int,input().split())
map = [list(map(int, input().split())) for _ in range(r)]
tmp = [0,0,0]
MAX = 0

com(0,0)

print(MAX)