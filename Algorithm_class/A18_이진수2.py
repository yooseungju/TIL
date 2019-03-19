import sys
sys.stdin = open('이진수2_input.txt')


T = int(input())

def solution(num):
    c = 13
    str_bin = ''
    while c > 0:
        if num * 2 == float(1):
            str_bin += '1'
            return str_bin
        else:
            num *= 2
            str_bin += str(int(num))
            num -= int(num)
            c -= 1
    return 'overflow'


for tc in range(T):
    num = float(input())
    print('#{} {}'.format( tc+1, solution(num)))