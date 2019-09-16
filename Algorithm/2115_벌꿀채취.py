import sys
sys.stdin = open('input.txt')


def get_max(cnt, P, s, RE):
    global tmp_MAX
    if tmp_MAX < RE:
        tmp_MAX = RE
    for i in range(s,M):
        if cnt + P[i] <= C:
            get_max(cnt+P[i], P, i+1, RE+(P[i]**2))

def check():
    global MAX, tmp_MAX
    tmp = 0
    for p in range(2):
        if sum(person[p]) <= C:
            for i in person[p]:
                tmp += (i**2)
        else:
            tmp_MAX = 0
            get_max(0,person[p],0,0)
            tmp += tmp_MAX
    if MAX < tmp:
        MAX = tmp

def com(n, k, sr, sc):
    if n == k:
        check()
        return
    j = sc

    for i in range(sr, N):
        while j <= (N-M):
            if not visited[i][j] :
                person[n] = [honey[i][m] for m in range(j, j+M)]
                for m in range(j,j+M):
                    visited[i][m] = 1
                com(n+1,k,i,j+M)
                for m in range(j,j+M):
                    visited[i][m] = 0
            j+=1
        j=0


T = int(input())
for tc in range(T):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    person = [0]*2
    visited = [[0]*N for _ in range(N)]
    tmp_MAX = 0
    MAX = 0
    com(0,2,0,0)
    print(f"#{tc+1} {MAX}")