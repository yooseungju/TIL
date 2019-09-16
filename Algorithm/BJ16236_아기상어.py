import sys
sys.stdin = open('input.txt')


dy = (-1,1,0,0)
dx = (0,0,-1,1)

# 거리에 따른 물고기를 찾는다.
def BFS(q):
    possible = []
    Min = 0xfffffff

    while q:
        x, y = q.pop(0)
        if visited[x][y] > Min:
            break

        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if M[nx][ny] == size or M[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

                elif M[nx][ny] < size:
                    visited[nx][ny] = visited[x][y] + 1

                    if possible:
                        if possible[0][0] < visited[nx][ny]:
                            return possible

                    possible.append((visited[nx][ny],nx,ny))
                    Min = visited[nx][ny]

    return possible


def find():
    for i in range(N):
        for j in range(N):
            if M[i][j] == 9:
                return (i,j)


N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

size = 2

flag = 1

time = 0

eat = 0


i, j = find()

while True:
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    legth_list = BFS([(i,j)])

    if len(legth_list) == 0:
        break

    M[i][j] = 0

    #eat!
    if len(legth_list) == 1:
        i = legth_list[0][1]
        j = legth_list[0][2]
        M[i][j] = 0
        eat += 1
        time += (legth_list[0][0]-1)

    # x우선 순위로 정렬하기
    else:
        legth_list = sorted(legth_list, key=lambda x:x[1])
        pre = legth_list[0]

        new = []
        for i in range(len(legth_list)):
            if legth_list[i][1] == pre[1]:
                new.append(legth_list[i])
            else:
                break

        #eat!
        if len(new) == 1:
            i = new[0][1]
            j = new[0][2]
            M[i][j] = 0
            eat += 1
            time += (new[0][0]-1)


        else:
            # y우선 순위로 정렬하기
            new = sorted(new, key=lambda x:x[2])
            i = new[0][1]
            j = new[0][2]
            M[i][j] = 0
            eat += 1
            time += (new[0][0]-1)

    if eat == size:
        eat = 0
        size += 1

print(time)