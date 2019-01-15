def ans(K, N):
    i = 1
    ans = 0
    while i < (len(N)-K):
        S = 0
        last = 0
        for j in range(i,i+K):
            if N[j] == 1:
                last = j
            S += N[j]

        if S > 0:
            i = last+1
            ans += 1
        else:
            return 0
    return ans


T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    N = [0]*(N+1)


    for i in list(map(int, input().split())):
        N[i] = 1


    print("#{} {}".format(tc+1, ans(K, N)))

