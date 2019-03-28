
import sys
sys.stdin = open('input.txt')


def BFS(s,g):
    Q = []

    dj = [-1,1,0,0]
    di = [0,0,-1,1]

    M[s[0]][s[1]] = 0
    Q.append(s)

    while len(Q)>0:

        q = Q.pop(0)
        if q == g:
            return M[q[0]][q[1]]
        for m in range(4):
            if q[0] + di[m] >= 0 and q[0] + di[m] < Y and q[1] + dj[m] >= 0 and q[1] +dj[m] < X and M[q[0] + di[m]][q[1] + dj[m]] == '0':
                M[q[0] + di[m]][q[1] + dj[m]] = M[q[0]][q[1]] + 1
                Q.append([q[0] + di[m],q[1] + dj[m]])



X, Y = map(int, input().split())
IN = list(map(int, input().split()))

s =[int(IN[1])-1, int(IN[0])-1]
g = [int(IN[3])-1, int(IN[2])-1]

M = [list(input()) for _ in range(Y)]
ans = BFS(s,g)
print(ans)











