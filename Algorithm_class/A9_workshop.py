
import sys
sys.stdin = open('input.txt')

SIZE = 100


def ans():
    s = input()
    matrix = [list(map(int, input().split())) for _ in range(SIZE)]
    count = 0


    for y in range(SIZE):
        temp = []
        for x in range(SIZE):
            if matrix[x][y] != 0:
                temp.append(matrix[x][y])

        if len(temp) > 2:
            for i in range(0, len(temp)-1):
                if temp[i:i+2] == [1,2]:
                    count += 1
    return count


for tc in range(10):
    print(f'#{tc+1} {ans()}')