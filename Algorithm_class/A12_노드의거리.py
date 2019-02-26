import sys
sys.stdin = open('노드의거리_input.txt')
T = int(input())



def BFS(v, G):
    global M
    queue = []
    queue.append(v)
    visited = [0] * (V + 1)
    visited[v] = 1

    while len(queue) != 0:
        t = queue.pop(0)
        for w in range(1, V + 1):
            if M[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
                if w == G:
                    return visited[w]-1
    return 0

for tc in range(T):
    V, E = map(int, input().split())
    M = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        k, v = map(int, input().split())
        M[k][v] = 1
        M[v][k] = 1

    S, G = map(int, input().split())
    print(f'#{tc+1} {BFS(S, G)}')