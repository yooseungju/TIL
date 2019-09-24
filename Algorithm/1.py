import sys
sys.stdin = open('input.txt')

n, C = map(int, input().strip().split(' '))
M = [int(input()) for _ in range(n)]
c = [0]*C
time = 0

while True:
    if M:
        for i in range(C):
            if not c[i]:
                c[i] = M.pop(0) -1
            else:
                c[i] -= 1

    else:
        flag = 0
        for i in range(C):
            if c[i]:
                c[i] -= 1
                flag = 1
            else:
                continue


        if not flag:
            break

    time += 1

print(time)
