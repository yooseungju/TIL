import sys
sys.stdin = open('input.txt')
N = int(input())
pre = 0
def binary_search(tree,s,pre):
    print(s, end = ' ')
    for i in range(len(tree[s])):
        binary_search(tree, tree[s][i], s)

tree = {x:[] for x in range(N+1)}
input_list = list(map(int , input().split()))


for i in range(0,len(input_list),2):
    tree[input_list[i]].append(input_list[i+1])

binary_search(tree, 1, 0)





