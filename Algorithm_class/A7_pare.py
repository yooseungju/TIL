
pares = list(input())

stack = []
cnt = 0
top = -1

for p in pares:
    if p == ")":
        while stack(top) != "(":
            stack.pop()
            top -= 1
        stack.pop()
        top -= 1


        stack.pop()
        cnt += 1
        top -= 1

    else:
        stack.append(p)
        top += 1

if top == -1:
    print(1)











