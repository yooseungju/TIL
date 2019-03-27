import sys

sys.stdin = open('A20_최대상금_input.txt')


def perm(n, c):
    global result, change
    if visited[c][int("".join(num))]:
        return
    else:
        visited[c][int("".join(num))] = 1
    # if k == len(num) - 1:
    #     return
    if change == c:
        money = int("".join(num))
        if result < money:
            result = money
    else:
        for i in range(n - 1):
            for j in range(i + 1, n):
                num[i], num[j] = num[j], num[i]
                # perm(n, k, c + 1)
                perm(n, c + 1)
                num[i], num[j] = num[j], num[i]
                # perm(n, k + 1, c)


T = int(input())
for tc in range(1, T + 1):
    num, change = input().split()
    change = int(change)
    num = list(num)
    visited = [[0 for _ in range(1000000)] for _ in range(change+1)]

    result = 0
    perm(len(num), 0)
    print('#{} {}'.format(tc, result))
