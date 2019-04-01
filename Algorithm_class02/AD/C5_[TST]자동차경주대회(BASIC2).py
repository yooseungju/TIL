import sys
sys.stdin = open('input.txt')


# def perm(k, n, TIME):
#     global MIN
#     if TIME > MIN:
#         return
#
#     if k == n:
#         if MIN > TIME:
#             MIN = TIME
#         return
#
#     else:
#         for i in range(N, k, -1):
#             SUM = 0
#             for j in range(k, i):
#                 if M[k][j] == 0:
#                     M[k][j] = M[k][j-1] + LIST[j]
#
#                 if  M[k][j] <= Max_l:
#                     perm(j+1, n, TIME + time[j])


def binarySearch(s, e, t):
    m = (s+e)//2
    if s >=e:
        return
    else:
        SUM = 0
        for i in range(e, m, -1):
            SUM += LIST[i]




MIN = 0xfffffff

Max_l =  int(input())
N = int(input())
LIST =  list(map(int, input().split()))
time = list(map(int, input().split()))

M = [[0] * N for _ in range(N)]

time.append(0)

print(MIN)