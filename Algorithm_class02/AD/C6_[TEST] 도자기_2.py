import sys
sys.stdin = open('input.txt')

def DFS(k, start):
    global sol, rec
    if k == M:
        sol += 1
        return
    for i in range(start, N):
        if rec[k] != arr[i]:
            rec[k] = arr[i]
            print(rec)
            DFS(k+1, i+1)
    rec[k] = 0


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    rec = [0]*M
    sol = 0
    arr.sort()
    DFS(0,0)
    print(sol)