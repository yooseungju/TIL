import sys
sys.stdin = open('input.txt')

T = int(input())

def BFS():
    Q =[(N,0)]

    while Q:
        current, cnt = Q.pop(0)
        if current == M:
            return cnt

        if current+1 < 1000001:
            Q.append((current+1,cnt+1))
        if current*2 < 1000001:
            Q.append((current*2,cnt+1))
        Q.append((current - 1, cnt + 1))
        Q.append((current - 10, cnt + 1))

for tc in range(T):
    N, M = map(int, input().split())
    MIN = BFS()
    print('#{} {}'.format(tc+1, MIN))