def postfix(tokens):
    stack = []
    profix_stack = []
    top = -1

    weight = {"*": 2 , "/": 2 , "(": 5 ,  "-": 1, "+":1}

    for token in tokens:
        if token.isdigit() or token.isalpha():
            profix_stack.append(token)

        elif token == ')':
            while top > -1 and stack[top] != '(':
                profix_stack.append(stack.pop())
                top -= 1
            stack.pop()
            top -= 1

        elif token != '(' and top > -1 and weight[token] >= weight[stack[top]]:
            profix_stack.append(token)

        else:
            stack.append(token)
            top += 1


    while top >= 0:
        profix_stack.append(stack.pop())
        top -= 1


    return profix_stack


if __name__ == '__main__':
    tokens = list(input().split())
    postfix(tokens)