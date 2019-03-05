import sys
sys.stdin = open('input.txt')

def pprint(Q):
    for i in range(len(Q)):
        for j in range(len(Q)):
            print("{}" .format(Q[i][j]), end = ' ' )
        print()


def turn(n):
    global Q
    for _ in range(n):
       Q = list(zip(*Q[::-1]))


N = int(input())
Q = [list(map(int, input().split())) for _ in range(N)]
flag = 0
while flag == 0:
    r = int(input())
    if r not in  [90 , 180 , 270 ,360]:
        break
    if r == 0:
        flag = 1
    else:
        turn(r//90)
        pprint(Q)


