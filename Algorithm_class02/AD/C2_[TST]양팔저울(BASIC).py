import sys
sys.stdin = open('input.txt')

def com(k, n, SUM):
    global flag

    if flag:
        return

    if sum(tmp) - (SUM*2)  == 0:
        flag = True
        return

    if k == n-1:
        return
    else:
        com(k+1, n, SUM+tmp[k])
        com(k + 1, n, SUM)



def power_set(k, n,b):
    global flag

    if flag:
        return

    if k == n:
        tmp.append(b)
        com(0, len(tmp),0)
        tmp.pop()
        return

    else:
        tmp.append(ci[k])
        power_set(k+1, n, b)
        tmp.pop()
        power_set(k+1, n, b)



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
        power_set(0, cN, b)

    if flag:
        print('Y', end = ' ')
    else:
        print('N', end = ' ')



