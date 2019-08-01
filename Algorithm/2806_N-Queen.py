import sys
sys.stdin = open('input.txt')

T = int(input())


def DFS(k, count):
    global ans

    if count < k:
        return

    if k == N:
        if count == N:
            ans += 1
        return


    for i in range(k,N):
        for j in range(N):
            if not crossRL[i+j] and not crossLR[i-j+N-1] and not col[j] and not row[i]:
                crossRL[i + j] = 1
                crossLR[i - j + N - 1] = 1
                col[j] = 1
                row[i] = 1

                DFS(k+1, count+1)

                crossRL[i + j] = 0
                crossLR[i - j + N - 1] = 0
                col[j] = 0
                row[i] = 0

        break





for tc in range(T):
    N = int(input())


    ans = 0


    crossLR = [0]*(N*2-1)
    crossRL = [0]*(N*2-1)

    row = [0]*N
    col = [0]*N


    DFS(0,0)


    print(f"#{tc+1} {ans}")