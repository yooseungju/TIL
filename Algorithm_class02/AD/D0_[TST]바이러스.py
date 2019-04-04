import sys
sys.stdin = open('input.txt')


def f(k):
    global cnt

    for i in range(N):
        if M[k][i] == 1 and visit[i] == 0:
            cnt += 1
            visit[i] = 1
            f(i)

N = int(input())
E = int(input())

M = [[0]*N for _ in range(N)]
cnt = 0
for i in range(E):
    s,e = map(int, input().split())
    M[s-1][e-1] = 1
    M[e - 1][s - 1] = 1

visit = [0] * N
visit[0] = 1
f(0)
print(cnt)
