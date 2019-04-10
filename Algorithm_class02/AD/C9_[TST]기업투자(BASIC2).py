def solution(s, N, M, cost):
    global maxcost

    if M < 0:
        return

    if s == N+1:
        # print(t)
        if cost > maxcost:
            maxcost = cost
        return

    for i in range(M):

        t[s-1] = data[i][s]
        solution(s+1, N, M-data[i][0], cost + data[i][s])
        t[s-1] = 0

    solution(s+1, N, M, cost)

M, N = map(int, input().split())
data = [list(map(int, input().split())) for i in range(M)]
# print(data)
chk = [0]*N
maxcost = 0
t = [0]*N
solution(1, N, M, 0)
print(maxcost)


