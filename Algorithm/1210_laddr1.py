import sys
sys.stdin = open("input.txt")

SIZE = 100


dy = (-1,1,0)
dx = (0,0,-1)

def DFS(i,j):
    Stack = [(i,j,2)]

    while len(Stack)>0:
        x, y, d = Stack.pop(0)

        if x == 0:
            return y

        if d != 2:
            while M[x][y] == 0:
                x = dx[d] + x
                y = dy[d] + y


        for m in range(3):
            if d == 1 and m == 0:
                continue
            elif d == 0 and m == 1:
                continue
            nx = dx[m] + x
            ny = dy[m] + y
            if 0 <= nx < SIZE and 0<=ny<SIZE:
                if M[nx][ny] == 1:
                    Stack.append((nx,ny,m))
                    break


def getStart():
    for i in range(SIZE-1, -1,-1):
        for j in range(SIZE-1,-1,-1):
            if M[i][j] == 2:
                return DFS(i,j)




for tc in range(10):
    t = input()
    M = [list(map(int, input().split())) for _ in range(SIZE)]

    print(f"#{tc+1} {getStart()}")

