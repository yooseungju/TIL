import sys

sys.stdin = open('input.txt')


T = 10
def ans(num,pow):
    global a
    if pow == 0:
        return 1
    else:
        return ans(num,pow-1)*num

for tc in range(T):
    x = input()
    num, pow = map(int, input().split())
    print('#{} {}'.format(tc+1, ans(num, pow)))