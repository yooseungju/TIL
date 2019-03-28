import sys
sys.stdin = open('input.txt')

N = int(input())

can= [[0 for _ in range(3)] for _ in range(4)]

def e():
    for _ in range(N):
        for id, i in enumerate(list(map(int, input().split()))):
            can[i][id] += 1
            can[0][id] += i
    flag = 0
    index = 3
    cnt_max = 0
    c = []
    while index > 0:
        if not flag:
            cnt_max = max(can[0])
            m = can[0].count(cnt_max)
            if m == 1:
                return can[0].index(cnt_max) + 1, cnt_max
            else:
                for _ in range(m):
                    c.append(can[0].index(cnt_max))
                    can[0][c[-1]] = 0
            flag = 1

        else:
            if len(c) == 2:
                if can[index][c[0]] > can[index][c[1]]:
                    return c[0]+1, cnt_max
                elif can[index][c[0]] < can[index][c[1]]:
                    return c[1]+1, cnt_max
                else:
                    index -= 1
            else:
                n_max = max(can[index])
                if can[index].count(n_max) == 1:
                    return can[index].index(n_max)+1, cnt_max
                if can[index].count(n_max) == 2:
                    c.pop(can.index(min(can[index])))
                else:
                    index -= 1
    return 0 , cnt_max

a,b = e()
print(a,b)