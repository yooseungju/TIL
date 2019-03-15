import copy
import sys
sys.stdin = open('input.txt')

T = int(input())

def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > N - 1:
        return True
    return False

def ans_DFS(table, start, end, sum):
    global cores, Min
    dj = [-1, 1, 0, 0]
    di = [0, 0, -1, 1]

    if start == end:
        if sum < Min:
            Min = sum
            return

    else:
        count = 0
        for m in range(4):
            tmp_table  = copy.deepcopy(table)
            tmp = []

            tmp.append([cores[start][0], cores[start][1]])

            while not isWall(tmp[-1][0] + di[m], tmp[-1][1] + dj[m]) and tmp_table[tmp[-1][0] + di[m]][tmp[-1][1] + dj[m]] == 0:
                tmp.append([tmp[-1][0] + di[m], tmp[-1][1] + dj[m]])
                # 가지치기
                if sum + len(tmp) > Min:
                    break

            if not isWall(tmp[-1][0] + di[m], tmp[-1][1] + dj[m]) and tmp_table[tmp[-1][0] + di[m]][tmp[-1][1] + dj[m]] == 1:
                count += 1

            elif not isWall(tmp[-1][0] + di[m], tmp[-1][1] + dj[m]) and tmp_table[tmp[-1][0] + di[m]][tmp[-1][1] + dj[m]] == 2:
                break

            if tmp[-1][0] == 0 or tmp[-1][0] == N - 1 or tmp[-1][1] == 0 or tmp[-1][1] == N - 1:
                cnt = len(tmp)
                while len(tmp) > 0:
                    t = tmp.pop()
                    tmp_table[t[0]][t[1]] = 2

                ans_DFS(tmp_table, start + 1, end, sum + cnt)
            else:
                count += 1

        if count == 4:
            ans_DFS(tmp_table, start + 1, end, sum)

for tc in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    cores = [[i, j] for i in range(1, N - 1) for j in range(1, N - 1) if M[i][j] == 1]
    Min = 100000
    ans_DFS(M ,0, len(cores), 0)
    print('#{} {}'.format(tc + 1, Min))