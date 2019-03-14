import sys
import copy
<<<<<<< HEAD

=======
>>>>>>> fe3f1a58aab97d126748510018f7910c6a64edf3
sys.stdin = open('input.txt')


T = int(input())

def isWall(x, y):
    if x< 0 or x> N-1 or y<0 or y > N-1:
        return True
    return False

<<<<<<< HEAD
def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > N - 1:
        return True
    return False


def ans_DFS(start, end, visited, sum):
    global cores, Min
    dj = [-1, 1, 0, 0]
    di = [0, 0, -1, 1]

    if start == end:
=======
def ans_DFS(start, end, visited, sum):
    global cores, Min
    dj = [-1,1,0,0]
    di = [0,0,-1,1]
    print(start)

    if start == end:
        print('ddd')
>>>>>>> fe3f1a58aab97d126748510018f7910c6a64edf3
        if sum < Min:
            Min = sum
        return

<<<<<<< HEAD
=======
    else:
        for m in range(4):
            tmp_visited = copy.deepcopy(visited)
            tmp = []

            if not isWall( cores[start][0]  + di[m], cores[start][1] + dj[m]) and M[cores[start][0]+di[m]][cores[start][1]+dj[m]] == 0 and visited[cores[start][0]+di[m]][cores[start][1]+dj[m]] == 0:
                tmp.append([cores[start][0] + di[m], cores[start][1] + dj[m]])
                while not isWall(tmp[-1][0]+di[m],tmp[-1][1]+dj[m]) and visited[tmp[-1][0]+di[m]][tmp[-1][1]+dj[m]] == 0 and M[tmp[-1][0]+di[m]][tmp[-1][1]+dj[m]] == 0:
                    tmp.append([tmp[-1][0]+di[m],tmp[-1][1]+dj[m]])
                    if sum + len(tmp) > Min:
                        break
                if tmp[-1][0] == 0 or tmp[-1][0] == N-1 or tmp[-1][1] == 0 or tmp[-1][1] == N-1:
                    cnt = len(tmp)
                    while len(tmp) > 0:
                        t = tmp.pop()
                        tmp_visited[t[0]][t[1]] = 1

                    ans_DFS(start + 1, end, tmp_visited, sum + cnt)
>>>>>>> fe3f1a58aab97d126748510018f7910c6a64edf3

    else:
        print(start)
        for m in range(4):
            tmp_visited = copy.deepcopy(visited)
            tmp = []

            if not isWall(cores[start][0] + di[m], cores[start][1] + dj[m]) and M[cores[start][0] + di[m]][
                cores[start][1] + dj[m]] == 0 and visited[cores[start][0] + di[m]][cores[start][1] + dj[m]] == 0:
                tmp.append([cores[start][0] + di[m], cores[start][1] + dj[m]])
                while not isWall(tmp[-1][0] + di[m], tmp[-1][1] + dj[m]) and visited[tmp[-1][0] + di[m]][
                    tmp[-1][1] + dj[m]] == 0 and M[tmp[-1][0] + di[m]][tmp[-1][1] + dj[m]] == 0:
                    tmp.append([tmp[-1][0] + di[m], tmp[-1][1] + dj[m]])

                    # 가지치기
                    if sum + len(tmp) > Min:
                        break

                if tmp[-1][0] == 0 or tmp[-1][0] == N - 1 or tmp[-1][1] == 0 or tmp[-1][1] == N - 1:
                    cnt = len(tmp)
                    while len(tmp) > 0:
                        t = tmp.pop()
                        tmp_visited[t[0]][t[1]] = 1

                    ans_DFS(start + 1, end, tmp_visited, sum + cnt)

for tc in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
<<<<<<< HEAD

    cores = [[i, j] for i in range(1, N - 1) for j in range(1, N - 1) if M[i][j] and (M[i][0] != 1 or M[i][N-1] != 1 or M[0][j] != 1 or M[N-1][j] != 1)]
    print(cores)


    visited = [[0 for _ in range(N)] for _ in range(N)]
    Min = 100000
    ans_DFS(0, len(cores), visited, 0)
    print('#{} {}'.format(tc + 1, Min))
=======

    cores = [[i,j] for i in range(1,N-1) for j in range(1,N-1) if M[i][j]]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    Min = 100000
    ans_DFS(0, len(cores), visited, 0)
    print('#{} {}'.format(tc+1, Min))
>>>>>>> fe3f1a58aab97d126748510018f7910c6a64edf3
