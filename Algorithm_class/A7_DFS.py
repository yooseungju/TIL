#1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# 인접행렬로 그래프 저장
G = [[0 for _ in range(8)] for _ in range(8)]
temp = list(map(int,input().split()))


visited = [0 for _ in range(8)]

for i in range(0,len(temp),2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1


for i in G:
    print(i)

def dfs(G, n):
    visited[n] = 1
    print(n)
    for i in range(8):
        if G[n][i] != 0 and visited[i] == 0:
            dfs(G, i)




print(dfs(G,1))