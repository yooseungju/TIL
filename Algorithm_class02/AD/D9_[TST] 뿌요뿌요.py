import sys
sys.stdin = open('input.txt')


def delete(startx, endx):
    for i in range(startx, endx+1):
        num_delete = counter[i]
        for j in range(num_delete):
            arr[i].pop(0)
            arr[i].append('.')
            counter[i] -= 1


def BFS(startx, starty):
    # 우 하
    dj = [1,0]
    di = [0,1]

    Q = [(startx,starty)]
    visited[startx][starty] = 1
    color = arr[startx][starty]
    counter[startx] += 1
    endx =  startx
    cnt = 1
    while Q:
        x, y = Q.pop(0)
        for m in range(2):
            nx = x + di[m]
            ny = y + dj[m]

            if 0 <= nx < 6 and 0 <= ny < 12:
                if arr[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    counter[nx] += 1
                    endx = nx
                    cnt += 1
                    Q.append((nx,ny))

    if cnt >= 4:
        delete(startx,endx)
        return True

    return False


T = int(input())
for _ in range(T):
    # 세로 12 가로 6
    tmp = [list(input()) for _ in range(12)]
    tmp = list(zip(*tmp[::-1]))
    arr = [list(i) for i in tmp]

    counter = {i:0 for i in range(6)}

    x = 0
    y = 0
    C = 0

    while x < 6:
        while y < 12:
            if arr[x][y] != '.':
                visited = [[0] * 12 for _ in range(6)]
                if BFS(x,y):
                    C += 1
                    y = 0
                    continue
                else:
                    y += 1
            else:
                y += 1
        y = 0
        x += 1

    print(C)






