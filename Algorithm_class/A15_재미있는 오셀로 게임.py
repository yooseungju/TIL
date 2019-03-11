import sys
sys.stdin = open('input.txt')

T = int(input())


def isWall(x,y):
    if x < 0 or x > N-1 or y < 0 or y > N-1:
        return True
    return False


def check(i, j, color):
    global N, M, flag
        # 좌 우 상 하 좌상, 좌하, 우상, 우하
    di = [0, 0, -1, 1, -1, 1, -1, 1]
    dj = [-1, 1, 0, 0, -1, -1, 1, 1]

    visited = [[0 for _ in range(N)]for _ in range(N)]

    M[i][j] = color
    visited[i][j] = 1

    stack = []
    stack.append([i, j, 0])
    flag = 1


    while len(stack) > 0:
        s = stack.pop(-1)





        for m in range(8):
            if not isWall(s[0]+di[m], s[1]+dj[m]) and visited[s[0]+di[m]][s[1]+dj[m]] == 0 and M[s[0]+di[m]][s[1]+dj[m]] != 0:
                visited[s[0] + di[m]][s[1] + dj[m]] = 1
                stack.append([s[0] + di[m], s[1] + dj[m], m])

                if s[0] != i and s[1] != j and M[s[0]][s[1]] == color:
                    while len(stack) > 0 and stack[-1][2] == color:
                        c = stack.pop(-1)
                        M[c[0]][c[1]] = color



for tc in range(T):
    N, C = map(int, input().split())

    M = [[0 for _ in range(N)] for _ in range(N)]


    M[N//2-1][N//2-1] = 2
    M[N // 2-1][N // 2] = 1
    M[N // 2][N // 2-1] = 1
    M[N // 2][N // 2] = 2

    for _ in range(C):
        i, j, color = map(int, input().split())
        flag = 0

        check(i-1, j-1, color)


    # print('#{} {} {}'.format(tc+1 , white, black))



