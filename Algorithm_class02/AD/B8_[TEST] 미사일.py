import sys
sys.stdin = open('input.txt')


def update(no):
    for i in range(N):
        temp = abs(arr[no][0] - arr[i][0]) + abs(arr[no][1] - arr[i][1])
        if temp <= R:
            arr[i][2] += P

def clear(no):
    for i in range(N):
        temp = abs(arr[no][0] - arr[i][0]) + abs(arr[no][1] - arr[i][1])
        if temp <= R:
            arr[i][2] -= P

def DFS(no):
    global sol

    if no == M:
        # 남아있는 군함의 개수
        cnt = 0
        for i in range(N):
            if arr[i][2] > 0: cnt+=1
        if cnt<sol:sol =cnt
        return
    for i in range(N): #군함
        if arr[i][2] <= 0: continue
        clear(i) # 현재 군함 반경이내 모든 군함 에너지 차감
        DFS(no+1)
        update(i) # 현재 군함 반경이내 모든 군함 에너지 복원

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M, P, R = map(int, input().split())
sol = 16
DFS(0)
print(sol)









