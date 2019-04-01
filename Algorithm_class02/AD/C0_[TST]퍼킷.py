import sys
sys.stdin = open('input.txt')

N = int(input())


def power_set(k, S, B):
    global MIN
    if k == N:
        if B != 0:
            if MIN == '':
                MIN = abs(S - B)

            elif abs(S-B) < MIN:
                MIN = abs(S-B)
    else:
        power_set(k+1, S*I[k][0], B+I[k][1])
        power_set(k+1, S, B)



I = [list(map(int, input().split())) for _ in range(N)]
MIN = ''
power_set(0,1,0)
print(MIN)
