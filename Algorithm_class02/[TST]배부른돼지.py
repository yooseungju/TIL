import sys
sys.stdin = open('input.txt')
T = int(input())

Ymin = 100
Nmax = 0

for _ in range(T):
    M , A = input().split()
    M = int(M)
    if A == 'Y':
        if Ymin > M:
            Ymin = M

    else:
        if Nmax < M:
            Nmax = M

if Ymin != 100 and Ymin > Nmax:
    print(Ymin)
else:
    print('F')












