import sys
sys.stdin = open('A20_컨테이너운반_input.txt')



def trans():
    SUM = 0

    for t in M_W:
        i = 0
        sub_min = 0xfffffff
        sub_min_idx = 0xfffffff

        while i < len(N_W):
            if t - N_W[i] >= 0 and sub_min > t - N_W[i]:
                sub_min = t - N_W[i]
                sub_min_idx = i
            i+=1
        if sub_min_idx != 0xfffffff:
            SUM += N_W[sub_min_idx]
            N_W.pop(sub_min_idx)

    return SUM


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    N_W =  list(map(int, input().split())) #화물들의 무게
    M_W = list(map(int, input().split())) #트럭의 용량


    print('#{} {}'.format(tc+1, trans()))