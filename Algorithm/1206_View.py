import sys
sys.stdin = open("input.txt")




for tc in range(10):
    N = int(input())
    l = list(map(int, input().split()))
    count = 0

    for i in range(2, N-2):

        tallest = max(l[i-2], l[i-1], l[i+2], l[i+1])

        if l[i] - tallest > 0:
            count += (l[i] - tallest)



    print(f"#{tc+1} {count}")

