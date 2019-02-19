import sys
sys.stdin = open('input_미로.txt')

T = int(input())

def find_2(maze):
    for x in range(size):
        for y in range(size):
            if maze[x][y] == '2':
                return (x,y)

def path(i , j):
    global stack, maze, flag

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    if maze[i][j] == '3':
        flag = 1
    else:
        for m in range(4):
            if i + dx[m] < 0 or j + dy[m] < 0:
                continue
            elif i + dx[m] >= size or j + dy[m] >= size:
                continue
            elif flag == 0 and maze[i + dx[m]][j + dy[m]] != '1':
                maze[i][j] = '1'
                path(i+dx[m], j+dy[m])


for tc in range(T):
    size = int(input())
    maze = [list(input()) for _ in range(size)]

    i, j = find_2(maze)

    flag = 0
    path(i, j)
    print(f'#{tc+1} {flag}')