import sys
sys.stdin = open("input.txt")
T = int(input())

def cnt():
    str1 = input()
    str2 = input()

    max = 0
    for i in str1:
        tmp = 0
        for j in str2:
            if i == j:
                tmp += 1
        if tmp > max:
            max = tmp
    return max


for tc in range(T):
    print(f'#{tc+1} {cnt()}')