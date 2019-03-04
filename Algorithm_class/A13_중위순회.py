import sys
sys.stdin = open('input.txt')

T =10
def inorder(tree, start , order):
    global tree_char
    if len(tree[start]) == 2:
        inorder(tree, tree[start][0], order)
        order.append(tree_char[start])
        inorder(tree, tree[start][1], order)
    elif len(tree[start]) == 1:
        inorder(tree, tree[start][0], order)
        order.append(tree_char[start])
    else:
        order.append(tree_char[start])
    return order






for tc in range(T):
    N = int(input())
    tree = {x:[] for x in range(N+1)}
    tree_char = [0 for _ in range(N+1)]

    for _ in range(N):
        input_list = input().split()
        k = int(input_list.pop(0))
        tree_char[k] = input_list.pop(0)
        for i in input_list:
            tree[k].append(int(i))



    print("#{} {}".format(tc+1, ''.join(inorder(tree, 1, []))))