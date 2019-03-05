import sys
sys.stdin = open('input.txt')




def bingo(n):
    global row, col, cross_1, cross_2
    for i in range(5):
        for j in range(5):
            if board[i][j] == n:
                row[i] += 1
                col[j] += 1
                if i == j:
                    cross_1 += 1
                if i + j == 4:
                    cross_2 += 1
                return

def ans():
    global cnt
    voice = 0
    for i in range(5):
        for j in range(5):
            voice += 1
            bingo(v[i][j])
            if cross_1 == 5 or cross_2 == 5:
                if cross_2 == 5 and cross_1 == 5:
                    cnt = 2
                else: cnt = 1

            if cnt + row.count(5) + col.count(5) >= 3:
                return voice



row = [0, 0, 0, 0, 0]
col = [0, 0, 0, 0, 0]
cross_1 = 0
cross_2 = 0
cnt = 0
board = [list(map(int, input().split())) for _ in range(5)]
v = [list(map(int, input().split())) for _ in range(5)]

print(ans())
