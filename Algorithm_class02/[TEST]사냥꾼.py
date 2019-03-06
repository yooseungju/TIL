import sys
sys.stdin = open('input.txt')

N = int(input())
M = [list(map(int, list(input()))) for _ in range(N)]



def isWall(x , y):
    if x < 0 or x > N-1 or y < 0 or y > N-1:
        return True
    return False

count = 0
def hunter(i, j, m):
    global M
    global count
    # 좌 우 상 하 우하 좌상 좌하 우상
    di = [0, 0, -1, 1, 1, -1, 1, -1]
    dj = [-1, 1, 0, 0, 1, -1, -1, 1]
    if isWall(i+di[m], j+dj[m]) or M[i+di[m]][j+dj[m]] == 0:
        return
    elif M[i + di[m]][j + dj[m]] == 2:
        count += 1
        M[i + di[m]][j + dj[m]] = 3
        hunter(i + di[m],j + dj[m], m)
    elif M[i + di[m]][j + dj[m]] == 3:
        hunter(i + di[m], j + dj[m], m)

    return



for i in range(N):
    for j in range(N):
        if M[i][j] == 1:
            for m in range(8):
                hunter(i, j , m)
print(count)