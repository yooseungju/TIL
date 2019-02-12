import sys
sys.stdin = open('input.txt')
T = 1

for tc in range(T):
    V, E = map(int, input().split())
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]

    visited = [0 for _ in range(V+1)]
    start = [0 for _ in range(V+1)]

    l = list(map(int,input().split()))

    for i in range(0,len(l),2):
        G[l[i]][l[i+1]] = 1

    print(G)



    for s in range(V+1):
        if s != 0:
            print(s)
            print(G[s][0:V+1])
            start[s] = G[s][0:V+1].count(1)





