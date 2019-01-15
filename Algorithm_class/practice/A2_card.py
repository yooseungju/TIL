from collections import Counter
T = int(input())

for tc in range(T):
    N = int(input())
    s = list(map(int, list(input())))

    Num = {}
    for i in s:
        if Num.get(i) == None:
            Num[i] = 1
        else:
            Num[i] += 1
    key = 0
    value = 1

    for k, v in Num.items():
        if v > value:
            value = v
            key =  k

    if value == 1:
        key = max(s)

    print("#{} {} {}".format(tc+1, key, value))













