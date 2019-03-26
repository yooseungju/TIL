import sys
sys.stdin = open('A20_최대상금_input.txt')


def toNumber(dummy):
    String = ''
    for i in dummy:
        String += str(i)

    return int(String)

def solution(dummy, n, cnt):

    global Max, Me
    if dummy in Me[cnt]:
        return
    else:
        Me[cnt].append(dummy[::])

    if cnt == n:
        Number = toNumber(dummy)
        if Number > Max:
            Max = Number
    else:
        for k in range(len(dummy)):
            i = 0
            while i < len(dummy):
                if k != i:
                    dummy[k], dummy[i] = dummy[i], dummy[k]
                    solution(dummy, n, cnt+1)
                    dummy[k], dummy[i] = dummy[i], dummy[k]
                i+=1


T = int(input())
for tc in range(T):
    IN = input().split()
    N = int(IN[1])
    dummy = list(map(int, list(IN[0])))
    Max = 0
    Me =[[] for _ in range(11)]
    solution(dummy, N, 0)
    print('#{} {}'.format(tc+1, Max))