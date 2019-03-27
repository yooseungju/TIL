import sys
sys.stdin = open('A20_최대상금_input.txt')


def solution(len_dummy, cnt):
    global Max, Me

    if Me[cnt][int(''.join(dummy))]:
        return
    else:
        Me[cnt][int(''.join(dummy))] = 1

    if cnt == N:
        Number = int(''.join(dummy))
        if Number > Max:
            Max = Number
    else:
        for i in range(len_dummy-1):
            for j in range(i+1, len_dummy):
                dummy[i], dummy[j] = dummy[j], dummy[i]

                solution(len_dummy, cnt+1)

                dummy[i], dummy[j] = dummy[j], dummy[i]


T = int(input())
for tc in range(T):
    dummy, N = input().split()
    N = int(N)
    dummy = list(dummy)

    Me =[[0 for _ in range(1000000)] for _ in range(N+1)]
    Max = 0
    solution(len(dummy), 0)
    print('#{} {}'.format(tc+1, Max))