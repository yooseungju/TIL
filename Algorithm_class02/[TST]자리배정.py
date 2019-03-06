import sys
sys.stdin = open('input.txt')



def seats(I,J, N):

    M = [[0 for _ in range(J)] for _ in range(I)]

    value = 1

    Dy = [1, 0, -1, 0]
    Dx = [0, 1, 0, -1]
    x = 0
    y = 0
    d = 0
    flag = 0

    while I > 0 or J > 0:
        i = 0
        j = 0

        if not flag:
            M[0][0] = value
            value += 1
            flag = 1
            j += 1

        if flag:
            if d == 0 or d == 2:
                while j < J:
                    x += Dx[d]
                    y += Dy[d]
                    M[x][y] = value
                    if value == N:
                        return x, y
                    value += 1
                    j += 1
                J -= 1
            elif d == 1 or d == 3:
                I -= 1
                while i < I:
                    x += Dx[d]
                    y += Dy[d]
                    M[x][y] = value
                    if value == N:
                        return x, y
                    value += 1
                    i += 1
        if d == 3:
            d = -1

        d += 1

I, J = map(int, input().split())
N = int(input())

if N > I*J:
    print(0)
else:
    a,b = seats(I,J,N)
    print(a+1, b+1)