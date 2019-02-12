import sys
sys.stdin = open('input.txt')

memo = [1]
def fact(n):
    global memo
    if n >= 1 and len(memo) <= n:
        memo.append(fact(n-1)*n)
    return memo[n]

T = int(input())
def ans():
    case = int(input())
    num_of_twenty = case//20
    cnt = 0

    for x in range(num_of_twenty,-1,-1):
        y = (case-x *20)//10
        cnt += fact(x + y)/(fact(x)*fact(y)) * (2**x)

    return cnt

for tc in range(T):
    factorial = [0, 1]
    print(f"#{tc+1} {int(ans())}")