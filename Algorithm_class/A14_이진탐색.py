import sys
sys.stdin = open("이진탐색_input.txt")

T = int(input())
def binarysearch(tree, index):
    global value
    global num

    if index > num:
        return
    if index*2 > num:
        tree[index] = value
        value += 1
    else:
        binarysearch(tree, index*2)
        tree[index] = value
        value += 1
        binarysearch(tree, index*2+1)


for tc in range(T):
    num = int(input())
    tree = [0 for _ in range(num+1)]
    value = 1
    binarysearch(tree, 1)
    print("#{} {} {}".format(tc+1,tree[1], tree[num//2]))


