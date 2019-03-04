def preorder(node):
    print('{}'.format(node), end = ' ')
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    preorder(tree[node][0])
    print('{}'.format(node), end = ' ')
    preorder(tree[node][1])

def postorder(node):
    preorder(tree[node][0])
    preorder(tree[node][1])
    print('{}'.format(node), end = ' ')

def pritTree():
    for i in range(1, V+1):
