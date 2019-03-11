import sys
sys.stdin = open("subtree_input.txt")

T = int(input())


def num_of_node(tree, f):
    if f in tree.keys():
        v = tree[f]
        if len(v) > 1:
            return num_of_node(tree, v[0]) + num_of_node(tree, v[1]) + 1
        else:
            return num_of_node(tree, v[0]) + 1
    else:
        return 1


for tc in range(T):
    x, f = map(int, input().split())
    tree_list = list(map(int, input().split()))
    tree = {}
    for i in range(0,len(tree_list),2):
        if tree_list[i] not in tree.keys():
            tree.update({tree_list[i]:[]})
        tree[tree_list[i]].append(tree_list[i+1])

    print(f"#{tc+1} {num_of_node(tree, f)}")