import sys
sys.stdin  = open('input.txt')


N = int(input())

l = [float(input()) for _ in range(N)]

Max_list = []

for j in range(N-1):
    tmp = []
    for i in range(j, N):
        if not tmp:
            tmp.append(l[i])
        else:
            tmp.append(tmp[-1]*l[i])

    if len(tmp)>1:
        Max_list.append(max(tmp))
    else:
        Max_list.append(tmp[len(tmp)-1])


print(round(max(Max_list), 3))