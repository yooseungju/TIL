import sys
sys.stdin = open('input.txt')

def com(k, n, SUM, chk):
    if k == n:
        return
    else:
        for i in range(n):
            if chk[i] == 0:



def power_set(k, n):
    global flag

    if flag:
        return

    if k == n:
        chk = [0] * len(tmp)
        com(0, len(tmp),0, chk)
        return

    else:
        tmp.append(ci[k])
        power_set(k+1, n)
        tmp.pop(0)
        power_set(k+1, n)



cN = int(input())
ci = list(map(int, input().split()))

bN = int(input())
bi = list(map(int, input().split()))
tmp = []
for b in bi:
    flag = False

    if b in ci:
        flag = True
    else:
        ci.append(b)
        power_set(0, cN, 0)

    if flag:
        print('Y', end = ' ')
    else:
        print('N', end = ' ')



