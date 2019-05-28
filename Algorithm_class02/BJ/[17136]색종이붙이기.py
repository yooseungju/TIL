import sys

sys.stdin = open('input.txt')
SIZE = 10


def check(x,y,k):
    for i in range(k):
        for j in range(k):
            nx = x+i
            ny = y+j
            if 0<=nx<SIZE and 0<=ny<SIZE:
                if M[nx][ny] != 1:
                    return False

    return True

def search(k, count, result, SUM):
    global Min

    if(k==0):
        if C - SUM != 0:
            return
        if result < Min:
            Min = result
        return

    flag = 1

    for i in range(SIZE):
        if flag:
            for j in range(SIZE):
                if M[i][j] == 1 and check(i,j,k):
                    if count < 5:

                        for x in range(k):
                            for y in range(k):
                                M[i+x][j+y] = 0

                        search(k, count+1, result, SUM)

                        for x in range(k):
                            for y in range(k):
                                M[i+x][j+y] = 1
                    flag = 0
                    break
        else:
            break

    search(k - 1, 0, result + count, SUM + (k ** 2) * count)


#main----------------------------------------------------------

Min = 0xfffffff
M = [list(map(int, input().split())) for _ in range(SIZE)]
C = 0
for i in range(SIZE):
    for j in range(SIZE):
        if M[i][j] == 1:
            C += 1
search(5, 0, 0, 0)

if Min == 0xfffffff:
    print(-1)
else:
    print(Min)
