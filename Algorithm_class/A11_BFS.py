def bfs(v):
    global G, V
    visited = [0] * (V+1)
    queue=[]
    queue.append(v)
    while len(queue) != 0:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=" ")
            for w in range(V+1):
                if G[v][w] == 1 and visited[w] == 0:
                    queue.append(w)

import sys
sys.stdin = open("연습3_input.txt")
V, E = map(int, input().split())

temp = list(map(int, input().split()))

G = [[0 for i in range(V+1)] for j in range(V+1)] #2차원 초기화


for i in range(0, len(temp), 2):  #입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(V+1):  #입력확인
    print("{} {}".format(i, G[i]))

bfs(1)
