import sys
sys.stdin = open('input.txt')

def DFS(cnt,s):
    global MIN

    if MIN < cnt:
        return

    if s > last:
        if MIN > cnt:
            MIN = cnt
        return

    for p in range(s,12):
        if plan[p]:
            DFS(cnt+(plan[p]*price[1]), p+1)
            DFS(cnt+price[2], p+1)
            DFS(cnt+price[3], p+3)
            break

T = int(input())
for tc in range(T):
    price = [0] + list(map(int,input().split()))
    tmp = [0]*12
    plan = list(map(int, input().split()))
    last = 0

    for i in range(11,-1,-1):
        if plan[i]:
            last = i
            break

    MIN = price[-1]

    DFS(0,0)
    print("#{} {}".format(tc+1,MIN))