import sys,itertools
sys.stdin = open('input.txt')

# 우 하 좌 상
dy = [1,0,-1,0]
dx = [0,1,0,-1]

def check(p):
    global MIN
    tmp_M = [M[i][::] for i in range(R)]

    for i in p:
        r,c,s = i
        fx, fy = (r - s - 1, c - s - 1 )

        visited =[[0]*C for _ in range(R)]
        one = 0
        s *= 2

        while s > 0:
            x = fx + one
            y = fy + one
            pre = tmp_M[x][y]
            for m in range(4):
                intro = 0
                while intro < s:
                    x += dx[m]
                    y += dy[m]
                    visited[x][y] = 1
                    pre, tmp_M[x][y] = tmp_M[x][y], pre
                    intro += 1
            one += 1
            s -= 2

    tmp_min = 0xfffffff
    for i in tmp_M:

        if tmp_min > sum(i):
            tmp_min = sum(i)


    if MIN > tmp_min:
        MIN = tmp_min


R, C , N = map(int, input().split())

M = [list(map(int, input().split())) for _ in range(R)]
po = [tuple(map(int, input().split())) for _ in range(N)]
tmp = [0]*N
perm = itertools.permutations(po,N)
MIN = 0xfffffff

for p in perm:
    check(p)

print(MIN)