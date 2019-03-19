import sys
sys.stdin = open('이진수_input.txt')


def my_bin(n):
    global ans
    str_bin = ''


    while n > 0:
        if n == 1:
            str_bin = str(n % 2) + str_bin
            break
        else:
            str_bin = str(n%2) + str_bin
            n = n//2

    if len(str_bin) < 4:
        str_bin = '0'*(4-len(str_bin)) + str_bin



    ans += str_bin



def solution(N, HEX):
    over_ten = {
        'A': 10, 'B': 11, 'C': 12,
        'D': 13, 'E': 14, 'F': 15
    }

    for h in HEX:
        if h.isdigit():
            my_bin(int(h))
        else:
            my_bin(over_ten[h])





T = int(input())
for tc in range(T):


    IN = input().split()
    N = int(IN[0])
    HEX = IN[1]
    ans = ''
    solution(N, HEX)


    print('#{} {}'.format(tc+1, ans))
