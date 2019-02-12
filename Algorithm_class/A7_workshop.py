import sys

sys.stdin = open("input.txt")


def ans():
    case = int(input())
    size = 100
    M = [list(map(int, input().split())) for _ in range(size)]

    j = M[99].index(2)

    for i in range(98, 0, -1):
        if j < 99 and j > 0:
            if M[i][j - 1] == 1:
                for J in range(j - 1, -1, -1):
                    if M[i][J] == 0:
                        j = J + 1
                        break
                    j =  0


            elif M[i][j + 1] == 1:
                if M[i][j + 1] == 1:
                    for J in range(j + 1, 100):
                        if M[i][J] == 0:
                            j = J - 1
                            break
                        j = 99


        elif j == 0:
            if M[i][j + 1] == 1:
                if M[i][j + 1] == 1:
                    for J in range(j + 1, 100):
                        if M[i][J] == 0:
                            j = J - 1
                            break

        elif j == 99:
            if M[i][j - 1] == 1:
                for J in range(j - 1, -1, -1):
                    if M[i][J] == 0:
                        j = J + 1
                        break
    return case, j

for tc in range(10):
    case, a = ans()
    print(f"#{case} {a}")