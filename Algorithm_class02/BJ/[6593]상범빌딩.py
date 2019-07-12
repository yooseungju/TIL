import sys
sys.stdin = open('input.txt')



def BFS(l,r,c):
    global result
    dx = (0, 0, -1, 1, 0, 0)
    dy = (-1, 1, 0, 0, 0, 0)
    dz = (0, 0, 0, 0, 1, -1)

    Q = [(l,r,c)]
    B[l][r][c] = 0
    while len(Q) > 0:
        z, x, y = Q.pop()

        for m in range(6):
            nz = z+dz[m]
            nx = x+dx[m]
            ny = y+dy[m]

            if 0<=nz<L and 0<=nx<R and 0<=ny<C:

                if B[nz][nx][ny] == '.':
                    B[nz][nx][ny] = B[z][x][y] + 1
                    Q.append((nz,nx,ny))

                elif B[nz][nx][ny] == 'E':
                    result = B[z][x][y] + 1
                    return

def find_S():
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if B[l][r][c] == 'S':
                    BFS(l, r, c)
                    return

#-----------------------------------------


L, R, C = map(int, input().split())

B = []


result = 0


for _ in range(L):
    B.append([list(input()) for _ in range(R)])
    input()


find_S()


if result != 0:
    print("Escaped in {} minute(s).".format(result))
else:
    print("Trapped!")




