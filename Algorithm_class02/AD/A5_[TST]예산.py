import sys
sys.stdin = open('input.txt')

N = int(input())
IN = list(map(int, input().split()))
IN.sort()
H = int(input())


def binarysearch(s, e, n):
    global MAX
    while s <= e:
        m = (s+e)//2
        if SUM + m*n < H:
            s = m+1
            if MAX < m:
                MAX = m
        elif SUM + m*n > H:
            e = m-1
        else:
            MAX = m
            return



MAX = 0
flag = False
SUM = 0
one = 1
i = 0


while 0 <= i < N:
    if one == 1 and SUM + IN[i] <= H:
        SUM += IN[i]
    elif one == -1:
        if SUM + (IN[i]*(N - i-1)) < H:
            binarysearch(IN[i], IN[i+1]-1, N-i-1)
            flag = True
            break
        else:
            SUM -= IN[i]
    else:
        one = -1
    i += one




if not flag:
    print(IN[-1])
else:
    print(MAX)



