import sys
sys.stdin = open('input.txt')


def com(k, TIME, pre):

    global MIN

    if sum(len_list[pre:k:-1]) > Max_l:
        return
    if k < 0:
        print(chk)
        if MIN > TIME:
            MIN = TIME
        return
    else:

        if k == N:
            chk[k] = 1
            com(k-1, TIME+time_list[k], k)
        else:
            chk[k] = 1
            com(k-1, TIME+time_list[k], k)
            chk[k] = 0
            com(k-1, TIME, pre)


MIN = 0xfffffff
Max_l =  int(input())
N = int(input())
len_list =  list(map(int, input().split()))
time_list = list(map(int, input().split()))
M = [[0] * N for _ in range(N)]

time_list.append(0)
chk = [0]*(N+1)


com(N,0,0)

print(MIN)