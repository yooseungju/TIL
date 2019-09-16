import sys
sys.stdin = open("input.txt")

# 움작이지않음 상 우 하 좌
dy = (0,0,1,0,-1)
dx = (0,-1,0,1,0)


def choice(n,v,idx,count):
    global max_count
    if n==2:
        if count > max_count:
            max_count =  count
        return

    for i in range(A):
        if visited[n][v][i] > 0:
            if i == idx:
                choice(n+1,v,i,count - (visited[n][v][i]//2))
            else:
                choice(n+1,v, i, count+visited[n][v][i])
        else:
            choice(n + 1, v, idx, count)


def solution():
    i = 1
    j = 1

    #사람 별
    for person in range(2):
        #사람들 움직임
        for m in range(M+1):
            idx = 0

            for k,v in AP.items():
                x, y = k
                c, p = v
                if abs(i-x) + abs(j-y) <= c:
                    visited[person][m][idx] = p
                idx += 1

            if m == M:
                break
            i = i + dx[move[person][m]]
            j = j + dy[move[person][m]]

        i = 10
        j = 10


T = int(input())

for tc in range(1):
    M, A = map(int,input().split())

    # 사람들의 움직임
    move = [list(map(int, input().split())) for _ in range(2)]
    # 방문 할 떄마다
    visited = [[[0]*A for _ in range(M+1)] for _ in range(2)]
    print(visited)
    AP = {}

    for _ in range(A):
        x,y,c,p = map(int, input().split())
        AP[(y,x)] = (c,p)

    solution()
    Max = 0



    for i in range(M+1):
        max_count = 0
        choice(0,i,0xfffffff,0)
        Max += max_count

    print("#{} {}".format(tc+1,Max))