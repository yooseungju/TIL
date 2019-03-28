import sys
sys.stdin = open('input.txt')


def ans():
    size = 211
    bomb = int(input())
    N = int(input())

    for _ in range(N):
        s, a = input().split()
        s = int(s)
        size -= s

        if size > 0:
            if a == 'T':
                bomb += 1
                if bomb > 8:
                    bomb %= 8
        else:
            return bomb


    if size > 0:
        return bomb


print(ans())











