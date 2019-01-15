T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    N = [0]*(N+1)


    for i in list(map(int, input().split())):
        N[i] = 1

    move = K
    ans = 0

    zero_cnt = 0

    for index, stop in enumerate(N):
        if zero_cnt < K:
            if stop == 1:
                if index+move+1 < len(N):
                    if 1 not in N[index+1 : index+move+1]:
                        ans += 1
                        move = K
                        zero_cnt = 0
                else:
                    if 1 not in N[index+1:]:
                        ans += 1
                        move = K
                        zero_cnt = 0
            else:
                zero_cnt += 1
                move -= 1
        else:
            ans = 0


    print("#{} {}".format(tc + 1, ans))












