

T = 10

def cross_max():
    arr = [[0 for _ in range(100)] for _ in range(100)]
    n = input()

    for i in range(100):
        arr[i] = list(map(int, input().split()))

    max_row = 0
    max_col = 0
    cross = 0

    for i in range(len(arr)):
        sum_row =0
        sum_col = 0
        sum_cross = 0
        for j in range(len(arr[i])):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
            if i == j:
                sum_cross = arr[i][j]
            if i+j == 99:
                sum_cross = arr[i][j]

        if max_row < sum_row:
            max_row = sum_row
        if max_col < sum_col:
            max_col = sum_col
        if cross < sum_cross:
            cross = sum_cross


    return max(max_row, max_col,cross)



for tc in range(T):

    print(f"#{tc+1}", cross_max())


for i in range(6):
    for j in range(6):
        if i == j:
            print("같을때", i, j)
        if i + j == 6:
            print("더해서:",i,j)