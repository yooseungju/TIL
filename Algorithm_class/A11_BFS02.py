def bfs(v):  # 1에서 가장 멀리 있는 정점을 찾으시오.
    global G, V
    queue=[]
    queue.append(v)  #enQueue하면서 방문처리
    visited[v] = 1
    print(v, end=" ")
    while len(queue) != 0:
        t = queue.pop(0)
        for w in range(1, V+1):
            if G[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
                print(w, end=" ")

import sys
sys.stdin = open("연습3_input.txt")
V, E = map(int, input().split())

temp = list(map(int, input().split()))

G = [[0 for i in range(V+1)] for j in range(V+1)] #2차원 초기화


for i in range(0, len(temp), 2):  #입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

visited = [0 for _ in range(V+1)]
# for i in range(V+1):  #입력확인
#     print("{} {}".format(i, G[i]))

bfs(1)
print(visited)

