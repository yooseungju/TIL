import sys
sys.stdin = open('input.txt')

def alive_sort():
    for i in range(N):
        for j in range(N):
            if len(alive[i][j]) > 1:
                alive[i][j].sort()


dy = (-1,1,0,0,1,1,-1,-1)
dx = (0,0,-1,1,-1,1,-1,1)
def year():
    #spring
    for i in range(N):
        for j in range(N):
            if alive[i][j]:
                # 양분 먹이기
                t = 0

                while t < len(alive[i][j]):
                    if feed[i][j] >= alive[i][j][t]:
                        feed[i][j] -= alive[i][j][t]
                        alive[i][j][t] += 1
                        t+= 1
                    else:
                        die[i][j] += (alive[i][j][t] // 2)
                        alive[i][j].pop(t)



    #summer
    for i in range(N):
        for j in range(N):
            if die[i][j]:
                feed[i][j] += die[i][j]
                die[i][j] = 0



    #fall
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            count = 0
            for a in range(len(alive[i][j])):
                if alive[i][j][a] % 5 == 0:
                    count += 1

            for m in range(8):
                x = i + dx[m]
                y = j + dy[m]
                if 0<=x<N and 0<=y<N:
                    tmp[x][y] += count


    for i in range(N):
        for j in range(N):
            if tmp[i][j]:
                alive[i][j]+= [1]*tmp[i][j]


    #winter
    for i in range(N):
        for j in range(N):
            if A[i][j]:
                feed[i][j] += A[i][j]


    alive_sort()

N, M, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

feed = [[5]*N for _ in range(N)]
die = [[0]*N for _ in range(N)]
alive = [[[]*1 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, a = map(int,input().split())
    alive[x-1][y-1].append(a)

alive_sort()

for _ in range(k):
    year()


ans = 0
for i in range(N):
    for j in range(N):
        if alive[i][j]:
            ans += len(alive[i][j])

print(ans)




