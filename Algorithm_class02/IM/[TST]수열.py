import sys
sys.stdin = open('input.txt')


def increase(i):
    global M, N
    length = 1
    pre = M[i]
    if N-i >= MAX:
        for x in range(i + 1 ,N):
            if M[x] < pre:
                return length
            else:
                length += 1
                pre = M[x]
    return length

def decrease(i):
    global M, N
    length = 1
    pre = M[i]
    if N-i >= MAX:
        for x in range(i + 1, N):
            if M[x] > pre:
                return length
            else:
                length += 1
                pre = M[x]
    return length

N = int(input())
M = list(map(int, input().split()))
MAX = 0
for i in range(N):
    l = increase(i)
    if l > MAX:
        MAX = l
    l = decrease(i)
    if l > MAX:
        MAX = l

print(MAX)
