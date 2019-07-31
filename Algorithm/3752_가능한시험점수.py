import sys
sys.stdin = open("input.txt")
T = int(input())



def com(k, SUM):
    global TMP
    if k < 0:
        if SUM not in TMP:
            TMP.append(SUM)
        return

    com(k-1, SUM+L[k])
    com(k-1, SUM)


for tc in range(T):
    N = int(input())
    L = list(set(map(int, input().split())))
    flag = False
    if N != len(L):
        flag = True

    TMP = []

    com(len(L)-1,0)

    if flag:
        print(f"#{tc+1} {len(TMP)+N-len(L)}")
    else:
        print(f"#{tc + 1} {len(TMP)}")