import sys
sys.stdin = open('미로의거리_input.txt')
T = int(input())

def BFS(G, i, j, SIZE):
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    visited = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    visited[i][j] = 1
    Q = []
    Q.append([i,j])

    while len(Q) != 0:
        t = Q.pop(0)
        for m in range(4):
            if t[0]+di[m] >= 0 and t[0]+di[m] < SIZE and t[1]+dj[m] >= 0 and t[1]+dj[m] < SIZE:
                if G[t[0]+di[m]][t[1]+dj[m]] == '0' and visited[t[0]+di[m]][t[1]+dj[m]] == 0:
                    Q.append([t[0]+di[m], t[1]+dj[m]])
                    visited[t[0]+di[m]][t[1]+dj[m]] = visited[t[0]][t[1]] + 1
                elif G[t[0]+di[m]][t[1]+dj[m]] == '3' and visited[t[0]+di[m]][t[1]+dj[m]] == 0:
                    visited[t[0] + di[m]][t[1] + dj[m]] = visited[t[0]][t[1]] + 1
                    for i in range(SIZE):
                        for j in range(SIZE):
                            print(visited[i][j], end=' ')
                        print()

                    return visited[t[0]][t[1]] - 1
    return 0


def maze():
    SIZE = int(input())
    G = [list(input()) for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            if G[i][j] == '2':
                return BFS(G, i, j, SIZE)




for tc in range(T):
    print(f'#{tc + 1} {maze()}')
