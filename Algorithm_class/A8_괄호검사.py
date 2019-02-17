import sys
sys.stdin = open("input.txt")

def ans():
    s = list(input())
    stack = []

    for i in s:
        if i == "}":
            while len(stack) > 0 and stack[-1] != "{":
                stack.pop()

            if len(stack) < 1:
                return 0
            else:
                stack.pop()

        elif i == ")":
            while len(stack) > 0 and stack[-1] != "(":
                stack.pop()
            if len(stack) < 1:
                return 0
            else:
                stack.pop()
        else:
            stack.append(i)

    if stack.count("{") + stack.count("(") > 0:
        return 0

    return 1

T = int(input())
for tc in range(T):
    print(f"#{tc+1} {ans()}")
