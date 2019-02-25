n = 10

def BFS(G, v):
    global visited
    queue = []
    queue.append(v)


    if visited[v] == 0:
        visited[v] = 1
        print(v)


    while queue:
        v = queue.pop(0)
        for i in range(1, len(G[v])):
            if G[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v]+1








N, E = 7, 8
a = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
li = list(map(int, a.split()))

G = [[0 for _  in range(N+1)] for _ in range(N+1)]
visited = [0]*(N+1)

for i in range(0, len(li), 2):
    G[li[i]][li[i+1]] = 1
    G[li[i+1]][li[i]] = 1


BFS(G, 1)
