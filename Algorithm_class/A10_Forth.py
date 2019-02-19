import sys
sys.stdin = open('input_Forth.txt')

T = int(input())

def ans():
    L= list(input().split())
    stack = []
    result = 0

    for l in L:
        if l.isdigit():
           stack.append(int(l))

        elif l != '.':
            if len(stack) > 1:
                if l == '+':
                   stack.append(stack.pop() + stack.pop())
                elif l == '-':
                    top1 = stack.pop()
                    top2 = stack.pop()
                    stack.append(top2 - top1)

                elif l == '*':
                    stack.append(stack.pop() * stack.pop())

                elif l == '/':
                    top1 = stack.pop()
                    top2 = stack.pop()
                    stack.append(top2 // top1)
            else:
                return 'error'
        else:
            if len(stack) != 1:
                result = 'error'
            else:
                result = stack.pop()

    return result

for tc in range(T):
    print(f'#{tc+1} {ans()}')