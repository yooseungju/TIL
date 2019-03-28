import sys
sys.stdin = open('input.txt')

def BFS(i,j):
    dj = [-1, 1, -1, 1, 2, 2, -2, -2]
    di = [2, 2, -2, -2, 1, -1, 1, -1]

    Q = []

    M[i][j] = 0

    Q.append([i,j])


    while len(Q) > 0:
        global Min

        q = Q.pop(0)
        if q == g:
            if Min > M[g[0]][g[1]]:
                Min = M[g[0]][g[1]]
            return

        for m in range(8):
            if q[0] + di[m] >= 0 and q[0] + di[m] < I and q[1] + dj[m] >= 0 and q[1] + dj[m] < J and M[q[0] + di[m]][q[1] + dj[m]] == '0':
                M[q[0] + di[m]][q[1] + dj[m]] = M[q[0]][q[1]] + 1
                Q.append([q[0] + di[m], q[1] + dj[m]])


I , J = map(int, input().split())

i, j , k, l = map(int, input().split())

Min = 0xfffffff

g = [k-1, l-1]

M = [['0']*J for _ in range(I)]


BFS(i-1, j-1)

print(Min)
