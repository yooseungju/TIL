import sys
sys.stdin = open('input.txt')

T = int(input())


def permutaion(sum, k, n):
    global min
    global check
    global matrix

    if k == n:
        if min > sum:
            min = sum

    else:
        for col in range(n):
            if check[col] == 0:
                if sum > min:
                    continue
                else:
                    check[col] = 1
                    sum += matrix[col][k]
                    permutaion(sum, k+1, n)
                    sum -= matrix[col][k]
                    check[col] = 0


for tc in range(T):
    min = 100
    sum = 0
    n = int(input())
    check = [0] * n
    matrix = [list(map(int, input().split())) for _ in range(n)]
    permutaion(sum, 0, n)

    print('#{} {}'.format(tc+1, min))


