T = int(input())


def cnt():
    M, N, x, y = map(int, input().split())
    """ 
        <M:N> 마지막 해
        <x,y> 해당해
        ans = 해당해가 몇번째 해인지 출력
             유효하지 않을때 -1
        x < M 이면 x' = x+1
        y < N 이면 y'= y+1

    """
    """ N 진법 """


    m = 1
    i = 1
    j = 1
    cnt = 0

    while (i, j) != (x, y):
        if not i < M:
            i == 1
            j += 1
        elif not j < N:
            j == 1
            i += 1
        else:
            i += 1
            j += 1

        cnt += 1


    return cnt




for tc in range(T):
    print(cnt())





