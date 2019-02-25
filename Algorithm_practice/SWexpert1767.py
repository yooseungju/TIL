import sys
sys.stdin = open('input.txt')

T = int(input())


def dfs(graph, start):
    visited = [0] * num
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited



for tc in range(T):
    num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(num)]

    cores = []

    for i in range(1,num-1):
        for j in range(1,num-1):
            if matrix[i][j] == 1:
                cores.append([i,j])

    visited = [0] * len(cores)


    print(f'#{tc+1} {}')