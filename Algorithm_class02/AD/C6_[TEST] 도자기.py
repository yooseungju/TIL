import sys
sys.stdin = open('input.txt')



def com(k):
    global cnt, TMP
    if len(tmp) > M:
        return
    if k == len(clay):
        if len(tmp) == M:
            if not tmp in TMP:
                TMP.append(tmp[::])
    else:

        # tmp.append(clay[k])
        # com(k+1)
        # tmp.pop()
        # com(k+1)

        if len(tmp) == 0:
            tmp.append(clay[k])
            com(k + 1)
            tmp.pop()
            com(k + 1)

        elif tmp[-1] <= clay[k]:
            tmp.append(clay[k])
            com(k+1)
            tmp.pop()
            com(k+1)
        else:
            com(k + 1)


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    clay = list(map(int, input().split()))
    clay.sort()
    tmp = []
    cnt = 0
    TMP = []

    com(0)
    print(len(TMP))
