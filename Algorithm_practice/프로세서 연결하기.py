import sys
sys.stdin = open('input.txt')

T = int(input())


def ans():
    print('ddd')


for tc in range(T):
    N = int(input())
    M = [ list(map(int, input().split())) for _ in range(N)]

    cores = [[i,j] for i in range(N) for j in range(N) if M[i][j]]

    print('#{} {}'.format(tc+1, ans()))