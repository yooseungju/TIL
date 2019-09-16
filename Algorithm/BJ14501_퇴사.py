import sys
sys.stdin = open('input.txt')

def DFS(start, money):
    global MAX

    if money > MAX:
        MAX = money


    for i in range(start, N+1):
        if (i + M[0][i]-1) <= N:
            visited[i] = 1

            DFS(i+M[0][i], money+M[1][i])

            visited[i] = 0


N =int(input())
M = [[0]*(N+1) for _ in range(2)]
visited = [0]*(N+1)
MAX = 0
for i in range(1,N+1):
    x, y  = map(int, input().split())
    M[0][i] = x
    M[1][i] = y


DFS(1,0)

print(MAX)
