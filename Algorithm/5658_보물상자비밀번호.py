import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(T):
    tmp = []

    N,K = map(int, input().split())
    length = N//4
    M = input()


    for j in range(length):
        for i in range(0,N,length):
            num = int("0x"+M[i:i+length],16)

            if num not in tmp:
                tmp.append(num)
        M = M[-1-j] + M

    tmp.sort(reverse=True)
    print(f"#{tc+1} {tmp[K-1]}")


