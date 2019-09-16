import sys
sys.stdin = open('input.txt')

T = int(input())


def check(i,j,pre):
    if M[i][j] - pre == 1:
        for x in range(X):
            if j-1-x < 0 or M[i][j-1-x] != M[i][j-1] or visited[i][j-1-x]:
                return False
        pre = M[i][j]
        j += 1

        return (j,pre)
    elif M[i][j]-pre == -1:
        for x in range(X):
            if j+x >= N or M[i][j+x] != M[i][j]:
                return False
        j += X
        pre = M[i][j-1]

        visited[i][j-1] = 1

        return (j, pre)

    elif M[i][j] - pre ==0:
        pre = M[i][j]
        j+=1
        return (j,pre)

    else:
        return False


def solution():
    global count
    for i in range(N):
        j = 1
        pre = M[i][0]

        flag = 1

        while j < N:
            result = check(i,j,pre)
            if result:
                j = result[0]
                pre = result[1]
            else:
                flag = 0
                break

        if flag:

            count += 1

for tc in range(T):
    count = 0
    N , X = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(N)]



    for _ in range(2):
        visited = [[0] * N for _ in range(N)]

        solution()

        M = list(zip(*M[::-1]))


    print(f"#{tc+1} {count}")