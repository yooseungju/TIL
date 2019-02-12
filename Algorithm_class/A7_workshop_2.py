import sys
sys.stdin = open("input.txt")


for tc in range(1, 11):
    dummy = int(input())
    data = [list(map(int, (input().split()))) for i in range(100)]

    y = 99
    x = data[99].index(2)
    while y > 0:
        y -= 1

        if x < 99 and data[y][x + 1] == 1:
            x += 1
            while data[y - 1][x] != 1:
                x += 1

        elif x > 0 and data[y][x - 1] == 1:
            x -= 1
            while data[y - 1][x] != 1:
                x -= 1

        elif y == 0:
            print("#{} {}".format(tc, x))