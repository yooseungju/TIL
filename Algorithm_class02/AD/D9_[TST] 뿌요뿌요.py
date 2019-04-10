import sys
sys.stdin = open('input.txt')


def delete():
    while dummy:
            j = dummy.pop()
            j.sort()
            while j:
                i = j.pop()
                arr[i[1]].pop(i[0])
                arr[i[1]].append('.')


def BFS(startx, starty):
    # 우 하
    dj = [-1,1,0,0]
    di = [0,0,-1,1]
    Q = [(startx,starty)]
    visited[startx][starty] = 1
    color = arr[startx][starty]

    temp = [(starty,startx)]
    while Q:
        x, y = Q.pop(0)
        for m in range(4):
            nx = x + di[m]
            ny = y + dj[m]

            if 0 <= nx < 6 and 0 <= ny < 12:
                if arr[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    temp.append((ny,nx))
                    Q.append((nx,ny))
    if len(temp) >= 4:
        dummy.append(temp)
        return


T = int(input())
for _ in range(T):
    # 세로 12 가로 6
    tmp = [list(input()) for _ in range(12)]
    tmp = list(zip(*tmp[::-1]))
    arr = [list(i) for i in tmp]
    x = 0
    y = 0
    C = 0
    puyo = True
    dummy = []
    while puyo:
        x = 0
        y = 0
        flag = 0
        visited = [[0] * 12 for _ in range(6)]
        while y < 12:
            while x < 6:
                if arr[x][y] != '.' and not visited[x][y]:
                    BFS(x,y)
                x += 1
            x = 0
            y += 1
        if not dummy:
            puyo = False
        else:
            C += 1
            delete()
    print(C)


