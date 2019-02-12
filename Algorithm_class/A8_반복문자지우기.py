import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    string = input()

    stack = []

    for char in string:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()

        else:
            stack.append(char)
    print(f"#{tc+1} {len(stack)}")