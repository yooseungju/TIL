import sys
sys.stdin = open('input.txt')
T = 10

def search(n):
    if len(tree[n]) < 2:
        return tree[n][0]

    if len(tree[n]) > 2:
        a = search(tree[n][1])
        b = search(tree[n][2])
        if tree[n][0] == '+':
            return a+b
        elif tree[n][0] == '-':
            return a - b
        elif tree[n][0] == '/':
            return a / b
        elif tree[n][0] == '*':
            return a * b


for tc in range(T):
    N = int(input())
    tree = {x:[] for x in range(N+1)}

    for _ in range(N):
        l = input().split()
        if len(l) > 2:
            tree[int(l[0])].append(l[1])
            tree[int(l[0])].append(int(l[2]))
            tree[int(l[0])].append(int(l[3]))
        else:
            tree[int(l[0])].append(int(l[1]))

    print("#{} {}".format(tc+1, int(search(1))))