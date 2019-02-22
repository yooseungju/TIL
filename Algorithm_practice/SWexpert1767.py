import sys
sys.stdin = open('input.txt')

T = int(input())

di = [0,0,0,0]



def backtraking(n, k):
    global min
    global cores
    global matrix
    global visited

    di = [0,0,-1,1]
    dj = [-1,1,0,0]

    if n == k:
        if min  > sum:
            min = sum

    else:
        for core in cores:
            # 좌
            if core[1] != cores[n][1]:
                cnt += 1
            # 우
            if core[1] != cores[n][1] and core[0] > cores[n][0]:
                cnt += 1
            # 상
            if core[1] != cores[n][1] and core[0] > cores[n][0]:
                cnt += 1
            # 하
            if core[1] != cores[n][1] and core[0] > cores[n][0]:
                cnt += 1






for tc in range(T):
    num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(num)]
    sum = 0
    k = 0
    min = 100
    cores = []
    visited = [0] * len(cores)
    for i in range(1,num-1):
        for j in range(1,num-1):
            if matrix[i][j] == 1:
                cores.append([i,j])


    print(cores)

    print(f'{tc+1} {min}')