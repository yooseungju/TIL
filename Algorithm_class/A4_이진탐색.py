import sys
sys.stdin = open("input.txt")
T = int(input())

def binarysearch(start, end, k):
    cnt = 0
    while (start <= end):
        cnt += 1
        middle = (start + end) // 2
        if middle == k:
            return cnt
        elif middle < k:
            start = middle
        else:
            end = middle


def winner():
    P, A, B = map(int, input().split())

    A_cnt = binarysearch(1, P, A)
    B_cnt = binarysearch(1, P, B)


    if A_cnt == B_cnt:
        return 0
    elif A_cnt < B_cnt:
        return 'A'
    elif  A_cnt > B_cnt:
        return 'B'


for tc in range(T):
    print(f"#{tc+1} {winner()}")