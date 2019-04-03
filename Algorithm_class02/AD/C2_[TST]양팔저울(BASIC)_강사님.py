import sys
sys.stdin = open('input.txt')


def DFS(no, Lsum, Rsum):
    global sol
    if Lsum == Rsum:
        sol = 1
        return
    if no == CN:
        return
    else:
        DFS(no+1, Lsum+chu[no], Rsum)
        DFS(no+1, Lsum, Rsum+chu[no])
        DFS(no+1, Lsum, Rsum)



#main --------------
CN = int(input())
chu = list(map(int, input().split()))

BN = int(input())
ball = list(map(int, input().split()))

for i in range(BN):
    sol = 0
    DFS(0, ball[i],0)
    if sol:print('Y', end=' ')
    else:print('N' , end=' ')


