import sys
sys.stdin = open('input.txt')

T = int(input())


def isWall(x,y):
    if x < 0 or x > N-1 or y < 0 or y > N-1:
        return True
    return False


def check(i, j, color):
    # print('돌놨다...',i,j,color)
    global N, M, flag
    # 좌 우 상 하 좌상, 좌하, 우상, 우하
    di = [0, 0, -1, 1, -1, 1, -1, 1]
    dj = [-1, 1, 0, 0, -1, -1, 1, 1]

    M[i][j] = color
    stack = []
    stack.append([i, j, 0])

    while len(stack) > 0:
        tmp = []
        find = 0

        if not flag:
            # 돌이 처음 들어왔을때 8방향을 확인하면서 stack에 담든다.
            s = stack.pop()
            for m in range(8):
                if not isWall(s[0] + di[m], s[1] + dj[m]) and M[s[0] + di[m]][s[1] + dj[m]] != 0 and M[s[0] + di[m]][s[1] + dj[m]] != color:
                    stack.append([s[0] + di[m], s[1] + dj[m], m])
                    # stack에 담는 값은  좌표, 방향
            flag = 1

        if flag:
            # 스택에 들어온 값에 대하여 같은 방향으로 탐색한다.
            s = stack.pop()
            tmp.append(s)
            i = s[0]
            j = s[1]

            # 방향을 이동한 값이 0이 아니면 tmp에 넣어준다.
            while not isWall(i + di[s[2]], j + dj[s[2]])  and  M[i + di[s[2]]][j + dj[s[2]]] != 0:
                i += di[s[2]]
                j += dj[s[2]]

                # 넣는 도중 같은 색을 찾으면  break tmp의 담던 것을 멈추고 tmp안 요소의 인덱스 해당값을 같은 색으로 바꿔준다
                if M[i][j] == color:
                    find = 1
                    break

                else:
                    tmp.append([i,j])

            # 색을 바꾸는 부분
            if find:
                while len(tmp) > 0:
                        t = tmp.pop()
                        M[t[0]][t[1]] = color


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
        check(j-1, i-1, color)

    black = 0
    white = 0


    for x in range(N):
        for y in range(N):
            if M[x][y] == 2:
                white += 1
            elif M[x][y] == 1:
                black += 1

    print('#{} {} {}'.format(tc+1, black, white))
