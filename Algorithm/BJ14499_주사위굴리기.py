# import sys
# sys.stdin = open('input.txt')
#
#
# dy = (0,1,-1,0,0)
# dx = (0,0,0,-1,1)
# row = [(1,0),(1,1),(1,2),(3,1)]
# col = [(0,1),(1,1),(2,1),(3,1)]
#
# def turn(o):
#     #동
#     if o == 1:
#         pre = DICE[row[0][0]][row[0][1]]
#         for i in range(1,4):
#             tmp = DICE[row[i][0]][row[i][1]]
#             DICE[row[i][0]][row[i][1]] = pre
#             pre = tmp
#         DICE[row[0][0]][row[0][1]] =pre
#     #서
#     elif o == 2:
#         pre = DICE[row[3][0]][row[3][1]]
#         for i in range(2,-1, -1):
#             tmp = DICE[row[i][0]][row[i][1]]
#             DICE[row[i][0]][row[i][1]] = pre
#             pre = tmp
#         DICE[row[3][0]][row[3][1]] = pre
#
#     #북
#     elif o == 3:
#         pre = DICE[col[3][0]][col[3][1]]
#         for i in range(2, -1, -1):
#             tmp = DICE[col[i][0]][col[i][1]]
#             DICE[col[i][0]][col[i][1]] = pre
#             pre = tmp
#         DICE[col[3][0]][col[3][1]] = pre
#
#     #남
#     else:
#         pre = DICE[col[0][0]][col[0][1]]
#
#         for i in range(1, 4):
#             tmp = DICE[col[i][0]][col[i][1]]
#             DICE[col[i][0]][col[i][1]] = pre
#             pre = tmp
#         DICE[col[0][0]][col[0][1]] = pre
#
#
#
# r, c ,x,y,k = map(int,input().split())
#
# M = [list(map(int, input().split())) for _ in range(r)]
# order = list(map(int, input().split()))
#
#
# DICE = [
#     ["#",0,"#"],
#     [0,  0,  0],
#     ["#",0,"#"],
#     ["#",0,"#"]]
#
#
# for e in range(k):
#     o = order[e]
#     nx = x + dx[o]
#     ny = y + dy[o]
#
#     if 0 <= nx <r and 0<=ny<c:
#         turn(order[e])
#
#         if not M[nx][ny]:
#                 M[nx][ny] = DICE[3][1]
#
#         else:
#             DICE[3][1] = M[nx][ny]
#             M[nx][ny] = 0
#
#         x = nx
#         y = ny
#
#         print(DICE[1][1])

import sys
sys.stdin = open('input.txt')


N, M, y, x, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

for i in range(len(direction)):
    if direction[i] == 1:
        if x+1 >= M: continue
        x += 1
        temp = dice[6]
        dice[6] = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[3]
        dice[3] = temp
        print(dice[1])
        if arr[y][x] == 0:
            arr[y][x] = dice[6]
        else:
            dice[6] = arr[y][x]
            arr[y][x] = 0


    if direction[i] == 2:
        if x-1 < 0: continue
        x -= 1
        temp = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = temp
        print(dice[1])
        if arr[y][x] == 0:
            arr[y][x] = dice[6]
        else:
            dice[6] = arr[y][x]
            arr[y][x] = 0

    if direction[i] == 3:
        if y-1 < 0 : continue
        y -= 1
        temp = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = temp
        print(dice[1])
        if arr[y][x] == 0:
            arr[y][x] = dice[6]
        else:
            dice[6] = arr[y][x]
            arr[y][x] = 0

    if direction[i] == 4:
        if y+1 >= N: continue
        y += 1
        temp = dice[6]
        dice[6] = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[2]
        dice[2] = temp
        print(dice[1])
        if arr[y][x] == 0:
            arr[y][x] = dice[6]
        else:
            dice[6] = arr[y][x]
            arr[y][x] = 0