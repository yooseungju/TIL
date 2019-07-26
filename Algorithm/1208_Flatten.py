import sys
sys.stdin = open("input.txt")


for tc in range(10):
    ans = 0



    N = int(input())
    l = list(map(int, input().split()))


    while N > 0:
        if max(l) - min(l) <= 1:
            break

        else:
            l[l.index(max(l))] -= 1

            l[l.index(min(l))] += 1

        N -= 1
    ans = max(l) - min(l)

    print(f"#{tc + 1} {ans}")