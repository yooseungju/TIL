import sys
sys.stdin = open('input.txt')


def check(i,j,n):

    tmp = []

    for x in range(n):
        for y in range(n):
            if M[i+x][j+y] == 1:
                M[i+x][j+y] = 0
                tmp.append([(i+x, j+y)])
            else:
                for t in tmp:
                    M[t[0]][t[1]] = 1
                return False
    return True

def back(i,j,n):
    for x in range(n):
        for y in range(n):
            M[i+x][j+y] = 1


def possible(i,j,n):
    if i+(n-1) < SIZE and j+(n-1) < SIZE:
        for x in range(n):
            for y in range(n):
                if M[i+x][j+y] == 0:
                    return False
        return True
    else:
        return False



def DFS(n, cnt, N):
    global MIN

    tmp = []
    if n == 0:
        if N != 0:
            MIN = -1
        elif MIN > cnt:
            MIN = cnt
        return

    for i in range(SIZE):
        for j in range(SIZE):
            if M[i][j] == 1:
                if n == 5:
                    N += 1
                if possible(i,j,n):
                    tmp.append((i,j))


    B = []
    if len(tmp) ==0:
        DFS(n-1, cnt, N)
    else:
        c = 0
        for t in tmp:
            chk = check(t[0], t[1],n)
            if chk:
                c += 1
                B.append((t[0],t[1]))

                if c >= 5:
                    break

        DFS(n-1, cnt+c, N-(n*n*c))

        for b in B:
            back(b[0],b[1],n)


memoi = [5] * 6
SIZE = 10
M = [list(map(int, input().split())) for _ in range(SIZE)]
MIN = 0xfffffff
DFS(5, 0, 0)
print(MIN)





