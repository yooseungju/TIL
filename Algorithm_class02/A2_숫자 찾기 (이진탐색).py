import sys
sys.stdin = open('input.txt')


N = int(input())
LIST = list(map(int, input().split()))
M = int(input())
M_LIST = list(map(int, input().split()))

start = 0
end = N

ans = 0
for m in range(M):
    start = 0
    end = N
    while start <= end:
        mid = (start+end)//2
        if LIST[mid] < M_LIST[m]:
            start = mid +1
        elif LIST[mid] > M_LIST[m]:
            end = mid - 1
        elif LIST[mid] == M_LIST[m]:
            ans = mid+1
            break
    if ans == 0:
        print(0)
    else:
        print(ans)




