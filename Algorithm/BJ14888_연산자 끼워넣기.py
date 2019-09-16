import sys
sys.stdin = open('input.txt')

def cal():
    global MIN, MAX
    ans = nums[0]
    for i in range(1,N):
        if tmp[i-1] == 0:
            ans += nums[i]
        elif tmp[i-1] == 1:
            ans -= nums[i]
        elif tmp[i-1] == 2:
            ans *= nums[i]
        else:
            if ans < 0:
                ans = -1*(abs(ans)//nums[i])
            elif ans == 0:
                ans == 0
            else:
                ans //= nums[i]

    if ans > MAX:
        MAX = ans
    if ans < MIN:
        MIN = ans

def DFS(n):
    if n == (N-1):
        cal()
        return
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            tmp[n] = i
            DFS(n+1)
            operators[i] += 1
            tmp[n] = 0


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
tmp = [0]*(N-1)
MIN = 1000000001
MAX = -(1000000001)
DFS(0)
print(MAX)
print(MIN)
