import sys
sys.stdin = open('input.txt')





def fill(w):
    for i in range(N):
        for j in range(N):
            if tmp_M[i][j] - w <= 0:
                tmp_M[i][j] = 0
            else:
                tmp_M[i][j] -= w

dx = (0,0,-1,1)
dy = (-1,1,0,0)

def check():
    global MAX
    visited = [[0]*N for _ in range(N)]
    v = 1
    for i in range(N):
        for j in range(N):
            if tmp_M[i][j] and not visited[i][j]:
                visited[i][j] = v
                q = [(i,j)]

                while q:
                    x, y = q.pop(0)
                    for m in range(4):
                        nx = x + dx[m]
                        ny = y + dy[m]
                        if 0<=nx<N and 0<=ny<N and tmp_M[nx][ny] and not visited[nx][ny]:
                            q.append((nx,ny))
                            visited[nx][ny] = v
                v+=1


    if MAX < (v-1):
        MAX = (v-1)



N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

l = 0xfffffff
r = 0
MAX = 0

for i in M:
    if l > min(i):
        l = min(i)
    if r < max(i):
        r = max(i)

for w in range(l-1,r+1):
    tmp_M = [M[i][::] for i in range(N)]
    fill(w)
    check()

print(MAX)
