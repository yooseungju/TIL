import sys
sys.stdin = open('input.txt')

T = int(input())

di = [0,0,0,0]



def backtraking(sum, n, k):
    global min
    global cores
    global matrix
    global visited

    di = [0,0,-1,1]
    dj = [-1,1,0,0]

    for i in range(1,n):
        for j in range(1,n):
            if matrix[i][j] == 1:
                for m in range(4):
                    if matrix[i+di[m]][j+dj[m]] == 0:














for tc in range(T):
    num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(num)]
    sum = 0
    k = 0
    min = 100
    cores = []
    visited = [0] * len(cores)



    print(f'{tc+1} {min}')