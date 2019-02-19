import sys
sys.stdin = open('input.txt')

T = 10

def ans(L):
    stack = []
    result = 0

    for l in L:
        if l.isdigit():
           stack.append(int(l))


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
    return stack[-1]

def postfix(tokens):
    stack = []
    profix_stack = []
    top = -1
    weight = {"*": 2, "/": 2, "(": 0 ,  "-": 1, "+":1}

    for token in tokens:
        if token.isdigit():
            profix_stack.append(token)

        elif token == '(':
            stack.append(token)
            top += 1

        elif token == ')':
            while top > -1 and stack[top] != '(':
                profix_stack.append(stack.pop())
                top -= 1
            stack.pop()
            top -= 1

        elif token != '(' and top > -1 and weight[token] <= weight[stack[top]]:
            while top > -1 and weight[stack[top]] >= weight[token]:
                profix_stack.append(stack.pop())
                top -= 1
            stack.append(token)
            top += 1

        else:
            stack.append(token)
            top += 1


    while top >= 0:
        profix_stack.append(stack.pop())
        top -= 1

    return profix_stack


for tc in range(T):
    length = input()
    tokens = list(input())
    post =  postfix(tokens)
    print(f'#{tc+1} {ans(post)}')