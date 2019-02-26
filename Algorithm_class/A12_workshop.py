import sys
sys.stdin = open('input.txt')


T = 10

def BFS(G, S):
    q = []
    result = []
    visited = [0]*(100+1)
    q.append(S)
    visited[S] = 1
    result = []


    while len(q) != 0:
        t = q.pop(0)
        for i in G[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

    Max = max(visited)
    return [i for i in range(len(visited)-1, -1, -1) if visited[i] == Max ][0]


for tc in range(T):
    L, S = map(int, input().split())

    G = {x:[] for x in range(100+1)}
    input_list = list(map(int, input().split()))

    for i in range(0,L,2):
        G[input_list[i]].append(input_list[i+1])


    print(f'#{tc+1} {BFS(G, S)}')
