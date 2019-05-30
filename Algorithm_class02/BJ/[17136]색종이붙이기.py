import sys

sys.stdin = open('input.txt')


def check(x,y,k):
    for i in range(k):
        for j in range(k):
            if x+i > 9 or y+j> 9 or M[x+i][y+j] == 0:
                return False
    return True

def change(x,y,k,v):
    for i in range(k):
        for j in range(k):
            M[i+x][j+y] = v

def search(c):
    global MIN

    if c > MIN:
        return

    count = 0

    for i in range(SIZE):
        for j in range(SIZE):
            count += 1
            if M[i][j] == 1:
                for k in range(5,0,-1):
                    if chk[k] > 0 and check(i,j,k):
                        change(i, j, k, 0)
                        chk[k] -= 1

                        search(c+1)

                        change(i, j, k, 1)
                        chk[k] += 1
                return


    if c < MIN:
        MIN = c
    return




#main----------------------------------------------------------
SIZE = 10
M = [list(map(int, input().split())) for _ in range(SIZE)]
C = 0

chk = [5]*6
MIN = 0xfffffff

search(0)

if MIN == 0xfffffff:
    print(-1)
else:
    print(MIN)