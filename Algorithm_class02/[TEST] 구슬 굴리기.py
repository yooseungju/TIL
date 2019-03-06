import sys
sys.stdin = open('input.txt')


I, J = map(int,input().split())

M = [list(map(int,list(input()))) for _ in range(I)]
change_d = int(input())
D = list(map(int, input().split()))
def isWall(x, y):
    if x < 0 or x > I-1 or y < 0 or y > J-1:
        return True
    return False
#1:상 2:하 3:좌 4:우
di = [0,-1,1,0, 0]
dj = [0,0,0,-1,1]

def roll(i , j):
    global M
    global count
    for m in D:
        flag = 0
        while flag == 0:
            if isWall(i+di[m], j + dj[m]) or M[i+di[m]][j+dj[m]] == 1:
                flag = 1
            elif M[i + di[m]][j + dj[m]] == 3:
                i = i + di[m]
                j = j + dj[m]
            else:
                count += 1
                i = i+di[m]
                j = j+dj[m]
                M[i][j] = 3
i = 0
j = 0
count = 1
for x in range(I):
    for y in range(J):
        if M[x][y] == 2:
            i = x
            j = y
M[i][j] = 3
roll(i,j)
print(count)



