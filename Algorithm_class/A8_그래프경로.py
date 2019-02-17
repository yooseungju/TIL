import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    G = {k:[] for k in range(1, V + 1)}

    for _ in range(E):
        k, v = map(int, input().split())
        G[k].append(v)

    S, D = map(int, input().split())

    flag = 0

    def move(start, D, G):
        global flag

        if D in G[start]:
            flag = 1
            return flag

        else:
            for s in G[start]:
                if flag == 0:
                    flag = move(s, D, G)
            return flag

    ans = move(S, D, G)

    print(f'#{tc+1} {ans}')