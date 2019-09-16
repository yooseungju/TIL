import sys
sys.stdin = open('input.txt')


def check(i,j,s):
    for x in range(i, i+s):
        for y in range(j, j+s):
            if not M[x][y]:
                return False
    return True

def paint(i,j,s,p):
    for x in range(i, i+s):
        for y in range(j, j+s):
            M[x][y] = p


def DFS(cnt, remain):
    global MIN

    if cnt >= MIN:
        return

    if remain == 0:
        if cnt < MIN:
            MIN = cnt
        return


    for i in range(S):
        for j in range(S):
            if M[i][j]:
                for s in range(5, 0, -1):
                    if i+s <= S and j+s <= S and check(i,j,s) and size[s] > 0:
                        size[s] -= 1
                        paint(i,j,s,0)

                        DFS(cnt + 1, remain - (s*s))

                        paint(i,j,s,1)
                        size[s] += 1
                return

S = 10
M = [list(map(int, input().split())) for _ in range(10)]

remain = [m.count(1) for m in M]

MIN = 0xfffffff
size = [0,5,5,5,5,5]

DFS(0,sum(remain))

if MIN < 0xfffffff:
    print(MIN)
else:
    print(-1)