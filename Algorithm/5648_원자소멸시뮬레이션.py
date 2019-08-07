T = int(input())


dx = (-1,1,0,0)
dy = (0,0,-1,1)

crush = {0:1, 1:0, 2:3, 3:2}

def BFS(q):

    len(q)



for _ in range(T):
    N = int(input())
    M = [[0]*3000 for _ in range(3000)]

    Q = []

    count = 0

    for _ in range(N):
        i, j, d,k =  map(int, input().split())
        Q.append((i,j,d))
        M[i+1000][j+1000] = (d,k)


    BFS(Q)


