import sys
sys.stdin = open('input.txt')

T = int(input())

def fanc(n):
    cnt = 0
    while n > 0:
        cnt += n % 10
        n = n//10
    return cnt


Max = [1000000,0]

for _ in range(T):
    num_char = input().strip()
    num = int(num_char)

    while num > 9:
        num = fanc(num)

    if Max[1] < num:
        Max = [int(num_char),num]
    elif Max[1] == num:
        if Max[0] > int(num_char):
            Max = [int(num_char),num]

print(Max[0])







