import sys
sys.stdin = open("input.txt")


T = int(input())



def ans():
    N, M ,node = map(int, input().split())


    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        index, x = map(int, input().split())
        tree[index] = x



    while N > 1 and tree[node] == 0:
        # 홀수
        if N%2 != 0:
            tree[N//2] = tree[N] + tree[N-1]
            N -= 2
        else:
            tree[N//2] = tree[N]
            N -= 1


    return tree[node]


for tc in range(T):
    print(f"#{tc+1} {ans()}")