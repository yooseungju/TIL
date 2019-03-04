import sys
sys.stdin = open('input.txt')

T = int(input())

def count_node(tree, start):
    global cnt
    cnt += 1
    for i in range(len(tree[start])):
        count_node(tree, tree[start][i])


def parent(N, p, tmp, pre):
    global flag
    if flag != 0:
        pass

    if not pre:
        if p[N] != []:
            tmp.append(p[N][0])
            parent(p[N][0], p, tmp, pre)
        return tmp

    elif p[N] != []:
        if p[N][0] in pre:
            flag = p[N][0]
        else:
            parent(p[N][0], p, tmp, pre)

    return



for tc in range(T):
    cnt = 0
    flag = 0

    V, E, N1, N2 = map(int, input().split())
    tree = {x: [] for x in range(V + 1)}
    p = {x: [] for x in range(V + 1)}
    input_list = list(map(int, input().split()))

    for i in range(0, len(input_list), 2):
        tree[input_list[i]].append(input_list[i + 1])
        p[input_list[i + 1]].append(input_list[i])

    N1_parent = parent(N1, p, [],[])

    parent(N2, p, [], N1_parent)
    count_node(tree, flag)


    print("#{} {} {}".format(tc+1, flag, cnt))