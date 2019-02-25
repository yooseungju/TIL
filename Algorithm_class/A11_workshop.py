import sys
sys.stdin = open('input.txt')

T = int(input())


def ans():
    N = int(input())

    M = [list(map(int, input().split())) for _ in range(N)]

    result = []
    col = 0
    row = 0
    col_flag = 200

    i = 0
    j = 0
    while i < N:
        if col_flag == 200:
            while j < N:
                if col == 0:
                    if M[i][j] != 0:
                        col_flag = j
                        col += 1
                        row += 1
                        M[i][j] = 0
                else:
                    if M[i][j] != 0:
                        col+=1
                        M[i][j] = 0
                    else:
                        j = 0
                        break
                j += 1
            i += 1
        else:
            if M[i][col_flag] != 0:
                row+=1
                index = 0
                while index < col:
                    M[i][col_flag+ index] =0
                    index += 1
            else:
                result.append([row, col])
                i = 0
                continue
            i += 1


    return result


















for tc in range(T):
    print(f'#{tc+1} {ans()}')