import sys
sys.stdin = open("input.txt")

T = int(input())


# 0 이동하지 않음 1좌   2하    3우    4상

dy = (0, -1, 0, 1, 0)
dx = (0, 0, 1, 0, -1)

for tc in range(1):

    M, N = map(int, input().split())
    for i in range(11):
        D = [[0]*11 for _ in range(11)]

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    BC = {i+1:() for i in range(N)}

    for i in range(1,N+1):
        y,x,c,p = map(int, input().split())
        BC[i]=(y,x,c,p)

    for i in range(11):
        for j in range(11):
            for b in range(1,N+1):
                if abs(i-BC[b][0]) + abs(j-BC[b][1]) <=  BC[b][2]:
                    if not D[i][j]:
                        D[i][j] = [b]
                    else:
                        D[i][j].append(b)

    ax, ay = (0, 0)
    bx, by = (10, 10)
    count = 0

    for n in range(M):
        ax += dx[A[n]]
        ay += dy[A[n]]


        bx += dx[B[n]]
        by += dy[B[n]]


        # 1개 일때
        # 2개 일떄
        # 3개 일떄





        













