import sys
sys.stdin = open('input.txt')

T = 10


def ans():
    M = [list(map(int, input().split())) for _ in range(100)]


    l_cross = 0
    r_cross = 0

    row = 0
    col = 0

    Max = 0

    i = 0
    j = 0
    
    while i < 100:
        while j < 100:
            row += M[i][j]
            col += M[j][i]
            if i ==j:
                l_cross += M[i][j]
            if i + j == 99:
                r_cross += M[i][j]

            j += 1

        if Max < max(row , col):
            Max = max(row, col)
        i += 1

    return max(Max, l_cross,r_cross)



for tc in range(T):
    t = input()
    print(f'#{t} {ans()}')