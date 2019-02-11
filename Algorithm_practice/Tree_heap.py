import sys
sys.stdin = open('input.txt')

def heap(tree):
    #자리 찾아 가기
    node = len(tree)-1

    while node > 1:
        parent = node//2
        if tree[node] < tree[parent]:
            tree[node], tree[parent] = tree[parent], tree[node]
        else:
            break
        node = parent
    return tree


def answer():
    l = int(input())
    ans = 0
    tree = [0]

    for i in list(map(int, input().split())):
        #가장 끝에 값 추가
        tree.append(i)
        tree = heap(tree)



    index = len(tree)-1
    while index > 1:
        index //= 2
        ans += tree[index]

    return ans

T = int(input())

for tc in range(T):
    print(f'#{tc+1} {answer()}')
