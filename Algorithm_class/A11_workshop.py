import sys
sys.stdin = open('input.txt')

T = int(input())

def insert(result, row_col):



    if not result:
        result.append(row_col[0])
        result.append(row_col[1])

    else:
        for i in range(0, len(result), 2):
            if result[i]*result[i+1] > row_col[0]*row_col[1]:
                result.insert(i, row_col[1])
                result.insert(i, row_col[0])
                return result
            elif result[i]*result[i+1] == row_col[0]*row_col[1]:
                if result[i] > row_col[0]:
                    result.insert(i, row_col[1])
                    result.insert(i, row_col[0])
                else:
                    result.insert(i+2, row_col[1])
                    result.insert(i+2, row_col[0])
                return result



        result.append(row_col[0])
        result.append(row_col[1])
    return result










def ans():
    N = int(input())

    M = [list(map(int, input().split())) for _ in range(N)]

    result = []
    col = 0
    row = 0
    col_flag = 200

    i = 0
    j = 0
    flag = False

    while i < N:
        if col_flag != 200 and M[i][col_flag] != 0:
            row += 1
            index = 0
            while index < col:
                M[i][col_flag+index] = 0
                index += 1
        elif col_flag != 200 and M[i][col_flag] == 0:
            # result.append([row, col])
            result = insert(result, [row,col])
            i = 0
            col_flag = 200
            row = 0
            col = 0
            flag = False
        if col_flag != 200 and j == N-1:
            # result.append([row, col])
            result = insert(result, [row, col])
            i = 0
            col_flag = 200
            row = 0
            col = 0
            flag = False

        while j < N and flag == False:
            if M[i][j] != 0:
                if col_flag == 200:
                    col_flag = j
                    row += 1
                col += 1
                M[i][j] = 0
            elif col_flag != 200 and (M[i][j] == 0):
                flag = True
                break
            if col_flag != 200 and j == N-1:
                flag = True
            j += 1
        j = 0
        i  += 1


    return len(result)//2, result




for tc in range(T):
    num, anslist = ans()
    anslist = list(map(str, anslist))


    print(f'#{tc+1} {num} {" ".join(anslist)}')