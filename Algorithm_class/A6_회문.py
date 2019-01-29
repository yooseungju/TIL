import sys
sys.stdin = open("input.txt")

T = int(input())

def find_pelindrome(char_list):
    length = len(char_list)
    middle = length//2
    if not length%2:
        if char_list[:middle] == char_list[:middle-1:-1]:
            return True
    else:
        if char_list[:middle] == char_list[:middle:-1]:
            return True
    return False

def answer():
    # N*N M글자수의 pellindrome
    N, M = map(int, input().split())
    arr = []

    for n in range(N):
        arr.append(list(input()))

    for i in range(N):
        for j in range(N):
            if j+M <= len(arr[i]):
                if find_pelindrome(arr[i][j:j + M]):
                    return ''.join(arr[i][j:j+M])

    for n in range(N):
        tmp = []
        for m in range(N):
            tmp.append(arr[m][n])
        for t in range(len(tmp)):
            if t + M <= N:
                if find_pelindrome(tmp[t:t+M]):
                    return ''.join(tmp[t:t+M])


for tc in range(T):
    print(f"#{tc+1} {answer()}")