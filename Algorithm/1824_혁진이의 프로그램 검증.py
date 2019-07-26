import sys
sys.stdin =  open("input.txt")

T = int(input())










dx = (-1,1,0,0)
dy = (0,0,-1,1)

def BFS():
    Q = [(0,0,1)]
    T[0][0][1] = 1

    while len(Q) > 0:
        x, y, d = Q.pop()
        nx = x+dx[d]
        ny = y+dy[d]

        if nx < 0:
            nx = R-1
        elif nx >= R:
            nx = 0

        if ny < 0:
            ny = C-1
        elif ny >= C:
            ny = 0

        # @	프로그램의 실행을 정지한다.
        if M[nx][ny] == ">":
            Q.append((nx, ny, 1))

        # <	이동 방향을 왼쪽으로 바꾼다.
        elif M[nx][ny] == "<":
            Q.append((nx,ny,0))

        # >	이동 방향을 오른쪽으로 바꾼다.
        elif M[nx][ny] == ">":
            Q.append((nx,ny,1))

        # ^	이동 방향을 위쪽으로 바꾼다.
        elif M[nx][ny] == ">":
            Q.append((nx, ny, 1))

        # v	이동 방향을 아래쪽으로 바꾼다.
        elif M[nx][ny] == ">":
            Q.append((nx, ny, 1))

        # _	메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
        elif M[nx][ny] == ">":
            Q.append((nx, ny, 1))

        # |	메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
        elif M[nx][ny] == ">":
            Q.append((nx, ny, 1))

        # ?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다. 방향이 바뀔 확률은 네 방향 동일하다.
        elif M[nx][ny] == ">":
            Q.append((nx, ny, 1))

        # .	아무 것도 하지 않는다.
        elif M[nx][ny] == ">":
            Q.append((nx, ny, 1))




        # +	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다.
        elif M[nx][ny] == ">":
            Q.append((nx, ny, 1))

        # -	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다.
        elif M[nx][ny] == ">":
            Q.append((nx, ny, 1))



        # 0~9	메모리에 문자가 나타내는 값을 저장한다.
        elif M[nx][ny] == ">":
            Q.append((nx, ny, 1))










for tc in range(T):
    R, C  = map(int, input().split())
    M = [list(input()) for _ in range(R)]
    T = [[[0,0,0,0] for _ in range(C)] for _ in range(R)]













