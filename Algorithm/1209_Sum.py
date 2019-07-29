import sys

sys.stdin = open("input.txt")


for tc in range(10):
    T = input()
    M = [list(map(int, input().split())) for _ in range(100)]

    crossLR = 0

    crossRL = 0

    MAX = 0


    for i in range(100):
        Row = 0
        Col = 0
        for j in range(100):
            Row += M[i][j]
            Col += M[j][i]

            if i == j:
                crossLR += M[i][j]

            if i + j == 99:
                crossRL += M[i][j]

        if MAX < max(Row, Col):
            MAX = max(Row, Col)

    if MAX < max(crossRL,crossLR):
        MAX = max(crossRL,crossLR)

    print(f"#{tc+1} {MAX}")







