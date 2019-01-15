T = int(input())

for tc in range(T):
    N = int(input())
    L = list(map(int, input().split()))

    Min = L[0]
    Max= L[0]

    for i in L[1:]:
        if Min > i:
            Min = i

    for j in L[1:]:
        if Max < j:
            Max = j

    ans = Max - Min


    print("#{} {}".format(tc + 1, ans))


