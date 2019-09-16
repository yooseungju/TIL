import sys
sys.stdin = open('input.txt')

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]


def check():
    global MIN
    A = 0
    B = 0

    for i in range(N):
        for j in range(N):
            if i != j:
                if i in tmp and j in tmp:
                    A += M[i][j]

                if not i in tmp and not j in tmp:
                    B+=M[i][j]


    if abs(A-B) < MIN:
        MIN = abs(A-B)


def com(n, s):
    if MIN == 0:
        return
    if n == (N//2):
        check()
        return

    for i in range(s,N):
        tmp[n] = i
        com(n+1,i+1)
        tmp[n] = 0

all = 0
for i in range(N):
    for j in range(N):
        if M[i][j]:
            all += M[i][j]

MIN = 0xfffffff
tmp = [0]*(N//2)
com(0,0)

print(MIN)