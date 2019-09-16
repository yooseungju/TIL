import sys
sys.stdin = open('input.txt')

N = int(input())
M = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
me = {}

for i in range(N):
    if M[i] not in me.keys():
        tmp = 1
        SUB = M[i] - B

        if SUB > 0:
            if SUB % C > 0:
                tmp += ((SUB//C)+1)
            else:
                tmp += (SUB//C)

        me[M[i]] = tmp
    cnt += me[M[i]]

print(cnt)