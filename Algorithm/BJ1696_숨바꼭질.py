import sys
sys.stdin = open("input.txt")

N, K = (1,100000)



def BFS(N):

    Q =[N]
    while Q:
        x = Q.pop(0)

        if x == K:
            print(visited[x])
            return

        if x < 0 or x > 100000:
            del visited[x]
            continue

        if not x+1 in visited.keys():
            visited[x+1] = visited[x] + 1
            Q.append(x+1)

        if not x-1 in visited.keys():
            visited[x-1] = visited[x] + 1
            Q.append(x-1)

        if not x*2 in visited.keys():
            Q.append(x*2)
            visited[x*2] = visited[x] + 1


visited = {N:0}

BFS(N)
