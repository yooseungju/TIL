import sys
sys.stdin = open('input.txt')


def power_set(k, cnt, SUM):
    global MIN

    if k == N:
        if cnt == N//2:
            if abs((sum(TL) - SUM) -SUM) < MIN:
                MIN = abs((sum(TL) - SUM) -SUM)
            return
    else:
        chk[k] = 1
        power_set(k+1, cnt+1, SUM + TL[k])
        chk[k] = 0
        power_set(k+1, cnt, SUM)

N  = int(input())
TL = list(map(int, input().split()))


MIN = 0xfffffff
chk = [0]*N
power_set(0,0,0)
print(MIN)