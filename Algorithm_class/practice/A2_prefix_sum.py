T = int(input())

for tc in range(T):
    N, P = map(int, input().split())
    L = list(map(int, input().split()))
    new_list = []


    for i in range(N-P+1):
        S = 0
        for j in range(i, i+P):
            S += L[j]

        new_list.append(S)


    print("#{} {}".format(tc+1, max(new_list)-min(new_list) ))