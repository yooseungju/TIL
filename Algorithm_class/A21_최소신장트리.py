INF = 0xfffffff

def MST_PRIM(G,s):
    key = [INF]*N
    pi = [None] * N
    visited = [False]*N
    for _ in range(N):
        minIndex = -1
        min = INF
        for i in range(N):
            if not visited[i] and key[i] < min:
                min = key[i]
                minIndex = i

        visited[minIndex]  = True

        for v, val in G[minIndex]:
            if not visited[v] and val < key[v]:
                key[v] = val
                po[v] = minIndex
