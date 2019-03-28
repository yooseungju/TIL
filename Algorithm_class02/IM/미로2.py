import sys
sys.stdin  = open('input.txt')

def find_start(M):
    global SIZE
    for i in range(SIZE):
        for j in range(SIZE):
            if M[i][j] == '2':
                return i,j

def maze(i, j):
    global M, flag
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    if flag == 1:
        return

    else:
        if M[i][j] == '3':
            flag = 1
        else:
            for m in range(4):
                if M[s[0]+di[m]][s[1]+dj[m]] == '0' or M[s[0]+di[m]][s[1]+dj[m]] == '3':
                    M[i][j] = '1'
                    maze(i+di[m],j+dj[m])

def maze(i, j):
    global M
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    stack = []
    stack.append([i,j])

    while len(stack) > 0:
        s = stack.pop(-1)

        if M[s[0]][s[1]] == '3':
            return 1
        else:
            for m in range(4):
                if M[s[0]+di[m]][s[1]+dj[m]] == '0' or M[s[0]+di[m]][s[1]+dj[m]] == '3':
                    M[s[0]][s[1]] = '2'
                    stack.append([s[0] + di[m], s[1]+dj[m]])

def maze(i, j):
    global M, SIZE
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    visited = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    visited[i][j] = 1

    Q = []
    Q.append([i,j])

    while len(Q) > 0:
        s = Q.pop(0)
        if M[s[0]][s[1]] == '3':
            return visited[s[0]][s[1]] -2



        else:
            for m in range(4):
                if 0<= s[0]+di[m] < SIZE and  0<= s[1]+dj[m] <SIZE:
                    if (M[s[0]+di[m]][s[1]+dj[m]] == '0' or M[s[0]+di[m]][s[1]+dj[m]] == '3'):
                        visited[s[0]+di[m]][s[1]+dj[m]] = visited[s[0]][s[1]]+1
                        M[s[0]][s[1]] = '2'
                        Q.append([s[0] + di[m], s[1]+dj[m]])



T = int(input())

for tc in range(T):
    SIZE = int(input())
    M = [list(input()) for _ in range(SIZE)]
    i , j = find_start(M)


    ans = maze(i,j)
    if not ans:
        ans = 0
    print('#{} {}'.format(tc+1, ans))