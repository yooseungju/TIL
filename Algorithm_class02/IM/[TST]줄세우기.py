import sys
sys.stdin = open('input.txt')


N = int(input())
ip = list(map(int, input().split()))
line = []
fill = 1
flag = 0

for id, num in enumerate(ip,1):
    if flag == 0:
        line.append(str(id))
        flag = 1
    else:
        fill -= num
        line.insert(fill, str(id))
        fill = len(line)


print(' '.join(line))







