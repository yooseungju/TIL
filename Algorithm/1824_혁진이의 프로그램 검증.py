import sys
sys.stdin =  open("input.txt")

T = int(input())


dy = (-1,1,0,0)
dx = (0,0,-1,1)

def ch(x, y, d):

    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 0:
        nx = R - 1
    elif nx >= R:
        nx = 0

    if ny < 0:
        ny = C - 1
    elif ny >= C:
        ny = 0

    return (nx,ny,d)

def BFS():
    global S
    Q = [(0,0,1)]

    while len(Q) > 0:
        x, y, d = Q.pop()

        if T[x][y][d][S]:
            if len(Q) == 0:
                return False

        # @	프로그램의 실행을 정지한다.
        if M[x][y] == "@":
            return True

        # <	이동 방향을 왼쪽으로 바꾼다.
        elif M[x][y] == "<":
            T[x][y][d][S] = 1
            Q.append(ch(x, y, 0))

        # >	이동 방향을 오른쪽으로 바꾼다.
        elif M[x][y] == ">":
            T[x][y][d][S] = 1
            Q.append(ch(x, y, 1))

        # ^	이동 방향을 위쪽으로 바꾼다.
        elif M[x][y] == "^":
            T[x][y][d][S] = 1
            Q.append(ch(x, y, 2))

        # v	이동 방향을 아래쪽으로 바꾼다.
        elif M[x][y] == "v":
            T[x][y][d][S] = 1
            Q.append(ch(x, y, 3))

        # _	메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
        elif M[x][y] == "_":
            T[x][y][d][S] = 1
            if S == 0:
                Q.append(ch(x, y, 1))
            else:
                Q.append(ch(x, y, 0))

        # |	메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
        elif M[x][y] == "|":
            T[x][y][d][S] = 1
            if S == 0:
                Q.append(ch(x, y, 3))
            else:
                Q.append(ch(x, y, 2))

        # ?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다. 방향이 바뀔 확률은 네 방향 동일하다.
        elif M[x][y] == "?":
            for m in range(4):
                Q.append(ch(x, y, m))
            T[x][y][d][S] = 1

        # .	아무 것도 하지 않는다.
        elif M[x][y] == ".":
            T[x][y][d][S] = 1
            Q.append(ch(x, y, d))

        # +	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다.
        elif M[x][y] == "+":
            if S == 15:
                S = 0
            else:
                S += 1
            T[x][y][d][S] = 1

            Q.append(ch(x, y, d))

        # -	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다.
        elif M[x][y] == "-":
            if S == 0:
                S = 15
            else:
                S -= 1
            T[x][y][d][S] = 1
            Q.append(ch(x, y, d))

        # 0~9	메모리에 문자가 나타내는 값을 저장한다.
        else:
            S += int(M[x][y])
            T[x][y][d][S] = 1
            Q.append(ch(x,y,d))





for tc in range(T):
    R, C  = map(int, input().split())
    M = [list(input()) for _ in range(R)]
    T = [[[[0 for _ in range(16)]for _ in range(4)] for _ in range(C)] for _ in range(R)]
    S = 0

    ans = BFS()

    if ans:
        ans = "YES"
    else:
        ans = "NO"

    print(f"#{tc+1} {ans}")













