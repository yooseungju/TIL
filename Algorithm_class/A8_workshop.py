import sys
sys.stdin = open('input.txt')
T = 10

for tc in range(T):
    V, E = map(int, input().split())

    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    start = [0 for _ in range(V+1)]
    temp = []


    l = list(map(int,input().split()))

    for i in range(0,len(l),2):
        G[l[i+1]][l[i]] = 1

    def dfs(G, k):
        global temp
        global visited

        temp.append(str(k))
        visited[k] = 1

        for y in range(1,V+1):
            if G[y][k] != 0 and visited[y] == 0:
                dfs(G, y)

    for x in range(1,V+1):
        start[x] = G[x].count(1)

    for s in range(1, V+1):
        if start[s] == 0:
            dfs(G, s)

    print(start)

    print(f"#{tc+1} {' '.join(temp)}")