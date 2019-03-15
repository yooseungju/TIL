import sys


sys.stdin = open("input.txt")
import copy

def find(idx, length, tables):
    global min_length, end

    # idx가 cores의 마지막 인덱스가 됐을 때 최소 길이 비교
    if idx == end:
        if length < min_length:
            min_length = length
        return


    else:
        y = cores[idx][0]
        x = cores[idx][1]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        count = 0

        # 4방향 탐색
        for i in range(4):
            flag = 0

            # table을 계속해서 참조하지 않고 재귀깊이마다 copytable을 생성(deepcopy)
            copytable = copy.deepcopy(table)

            for h in range(1, N):
                nx = x + dx[i] * h
                ny = y + dy[i] * h

                if copytable[ny][nx] == 0:
                    if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                        flag = 1
                        # 연결 되는 선을 2로 마킹한다.
                        for j in range(1, h + 1):
                            copytable[y + dy[i] * j][x + dx[i] * j] = 2
                        break

                elif copytable[ny][nx] == 1:
                    count += 1
                    break
                else:
                    break

            # 탐색 성공
            if flag == 1:
                find(idx + 1, length + h, copytable)

        # 프로세서의 4방향 탐색이 모두 실패하였을 때 재귀를 빠져나오지 않고 들어간다.
        if count == 4:
            find(idx + 1, length, copytable)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    table = [list(map(int, input().split())) for i in range(N)]
    cores = [[i, j] for i in range(1, N - 1) for j in range(1, N - 1) if table[i][j] == 1 ]

    min_length = 10000

    end = len(cores)

    find(0, 0, table)

    print("#{} {}".format(tc, min_length))