import sys
sys.stdin = open('input.txt')


stack= list(input())


open_cnt = 0

SUM = 0
while len(stack) > 0:
    s = stack.pop(-1)
    if s == ')':
        if stack[-1] == '(':
            SUM += open_cnt
            stack.pop(-1)
        else:
            open_cnt += 1
    elif s == "(":
        SUM += 1
        open_cnt -= 1


print(SUM)

