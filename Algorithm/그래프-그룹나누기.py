import sys
sys.stdin = open('input.txt')


def DFS(s):
    for i in range(N):
        if M[s][i] and not visited[i]:
            visited[s] = 1
            visited[i] = 1
            DFS(i)

T = int(input())

for tc in range(T):
    N, E = map(int,input().split())
    M = [[0]*N for _ in range(N)]
    L = list(map(int,input().split()))

    for i in range(0,len(L),2):
        M[L[i]-1][L[i+1]-1] = 1
        M[L[i+1]-1][L[i]-1] = 1

    visited = [0]*N
    ans = 0

    for n in range(N):
        if not visited[n]:
            DFS(n)
            ans += 1

    print("#{} {}".format(tc+1, ans))




