import sys
sys.stdin = open('input.txt')

def cal(temp):
    result = 0

    for i in range(len(temp)):
        for j in range(len(temp)):
            if i != j:
                result += M[temp[i]][temp[j]]
    return result


def check():
    global MIN

    tmp_2 = []
    for i in range(N):
        if i not in tmp:
            tmp_2.append(i)

    A = cal(tmp)
    B = cal(tmp_2)

    if abs(A-B) < MIN:
        MIN = abs(A-B)

def com(n,k,s):
    if MIN == 0:
        return

    if n == k:
        check()
        return
    for i in range(s,N):
        tmp[n] = i
        com(n+1,k,i+1)
        tmp[n] = 0

T= int(input())

for tc in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    all = 0
    for i in range(N):
        all += sum(M[i])
    h = N//2
    MIN = 0xfffffff
    tmp = [0]*h

    com(0,N//2,0)

    print(f"#{tc+1} {MIN}")