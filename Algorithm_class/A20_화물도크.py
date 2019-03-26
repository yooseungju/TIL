import sys
sys.stdin = open('A20_화물도크_input.txt')


T = int(input())
for tc in range(T):
    N = int(input())
    Sc = []

    for _ in range(N):
        S, E = map(int, input().split())
        Sc.append([S,E])

    Sc.sort(key=lambda m:m[1])
    sc_idx = 1
    pre = Sc[0]
    cnt = 1
    while sc_idx < N:
        if pre[1] <= Sc[sc_idx][0]:
            cnt += 1
            pre = Sc[sc_idx]
        sc_idx += 1
    print('#{} {}'.format(tc+1,cnt))

