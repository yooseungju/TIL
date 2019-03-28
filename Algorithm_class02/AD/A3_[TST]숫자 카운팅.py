import sys
sys.stdin = open('input.txt')



N = int(input())
LIST = list(map(int, input().split()))
M = int(input())
M_LIST = list(map(int, input().split()))

ans = 0

def binarySearch1(m, s, e):
    global lower
    while s <= e:
        mid = (s + e) // 2
        if LIST[mid] > M_LIST[m]:
            e = mid-1
        elif LIST[mid] < M_LIST[m]:
            s = mid+1
        else:
            if mid < lower:
                lower = mid
        e = mid-1

def binarySearch2(m, s, e):
    global upper
    while s <= e:
        mid = (s + e) // 2
        if LIST[mid] > M_LIST[m]:
            e = mid-1
        elif LIST[mid] < M_LIST[m]:
            s = mid+1
        else:
            if mid > upper:
                upper = mid
        s = mid + 1

for m in range(M):
    lower = 200000
    upper = -1

    binarySearch1(m, 0, N-1)
    binarySearch2(m, 0, N-1)

    if lower == upper:
        print(1, end=' ')
    elif upper == -1:
        print(0, end=' ')
    else:
        print(upper-lower+1, end = ' ')

