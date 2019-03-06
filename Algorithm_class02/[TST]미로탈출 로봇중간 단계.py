import sys
sys.stdin = open('input.txt')

N = int(input())
M = [list(input()) for _ in range(N)]
D = list(map(int, input().split()))

di = [0,1,0,-1,0]
dj = [0,0,-1,0,1]
flag = 0
i = 0
j = 0
count = 0
d = 0

def isWall(x, y):
    if x < 0 or x > N-1:return True
    if y < 0 or y > N-1:return True
    return False

while flag == 0:
    if isWall(i + di[D[d]], j+dj[D[d]]):
        d += 1
    elif M[i + di[D[d]]][j + dj[D[d]]] == '1':
        d += 1
    elif M[i + di[D[d]]][j + dj[D[d]]] =='2':
        flag = 1
    else:
        M[i][j] = '2'
        i += di[D[d]]
        j += dj[D[d]]
        count += 1
    if d == 4:
        d = 0
print(count)