import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(T):
    N = int(input())
    L = list(map(int, input().split()))

    store = [False]*10001
    store[0] = True
    count = 1

    for i in range(len(L)):
        c = count
        true = []

        for j in range(10001):
            if store[j]:
                if not store[j+L[i]]:
                    true.append(j+L[i])
                    count += 1
                c -=1

            if c == 0:
                break

        for z in true:
            store[z] = True

    print(f"#{tc + 1} {count}")