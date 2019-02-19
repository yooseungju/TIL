import sys
sys.stdin = open("input.txt")



def subset(N, K):
    arr = range(1,13)
    result = 0




    for i in range(1, 1<<len(arr)):
        sum = 0
        cnt = 0
        for j in range(len(arr)):
            if i & (1 << j):
                sum += arr[j]
                cnt += 1

        if sum == K and cnt == N:
            result +=1

    return(result)


T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    print(f"#{tc+1} {subset(N,K)}")

