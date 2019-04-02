import sys

sys.stdin  = open('input.txt')


def BFS(i, j):

    dj = [-1,1,0,0]
    di = [0,0,-1,1]

    Q = [[i,j,0]]
    visited[i][i][0] = 1


    while len(Q) > 0:
        q = Q.pop(0)

        if q[0] == N-1 and q[1] == M-1:
            return visited[q[0]][q[1]][q[2]]

        for m in range(4):
            if q[0]  + di[m] >= 0 and q[1] + dj[m] >=0 and q[0]  + di[m] < N and q[1]+dj[m]< M:
                if G[q[0]  + di[m]][q[1] + dj[m]] == 0 and visited[q[0] + di[m]][q[1] +dj[m]][0] == 0:
                    visited[q[0]+di[m]][q[1]+dj[m]][0] =  visited[q[0]][q[1]][q[2]]+1
                    Q.append([q[0] + di[m],q[1] + dj[m],0])

                elif G[q[0]+di[m]][q[1]+dj[m]] == 1 and visited[q[0]+di[m]][q[1]+dj[m]][1] == 0  and q[2] == 0 :
                    visited[q[0] + di[m]][q[1] + dj[m]][1] = visited[q[0]][q[1]][q[2]]+1
                    Q.append([q[0]+di[m], q[1]+dj[m], 1])

    return

N, M = map(int , input().split())
G = [list(map(int,list(input()))) for _ in range(N)]

visited = [[[0]*2 for _  in range(M)] for _ in range(N)]

print(BFS(0,0))
for v in visited:
    print(v)
print()