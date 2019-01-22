import sys

sys.stdin = open("input.txt")

T = int(input())





def painting():
    cnt = 0;
    arr = [[0 for _ in range(10)] for _ in range(10)]
    num = int(input())

    for _ in range(num):
        r1, c1, r2, c2, color = map(int,input().split())

        r = min(r1, r2)
        l = max(r1, r2)

        t = max(c1, c2)
        b = min(c1,c2)

        for i in range(r, l+1):
            for j in range(b,t+1):
                if arr[i][j] != 0:
                    cnt += 1
                arr[i][j]  = color

    return cnt







for tc in range(T):
    print(f"#{tc+1} {painting()}")




