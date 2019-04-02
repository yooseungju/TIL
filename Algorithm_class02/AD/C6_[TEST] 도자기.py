import sys
sys.stdin = open('input.txt')



def com(k):
    global cnt
    if len(tmp) > M:
        return
    if k == len(clay):
        if len(tmp) == M:
            print(tmp)

            cnt += 1
    else:
        tmp.append(clay[k])
        com(k+1)
        tmp.pop()
        com(k+1)

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    clay = list(map(int, input().split()))
    tmp = []
    cnt = 0
    com(0)

    D = [0] * 27

    print(cnt)