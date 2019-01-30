import sys
sys.stdin = open("input.txt")



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
    long = 0
    arr = []
    #이차원 배열을 만든다.
    for _ in range(100):
        arr.append(list(input()))


    #가로를 탐색
    for i in range(100):
        flag = 0
        while flag == 0:
            rMax = 100
            for j in range(100):
                if j + rMax <= 100:
                    if find_pelindrome(arr[i][j:j + rMax]):
                        flag = 1
                        if rMax > long:
                            long = rMax
                        break
                    rMax -= 1


    # 세로를 탐색
    for n in range(100):
        tmp = []
        for m in range(100):
            tmp.append(arr[m][n])

        flag = 0
        while flag == 0:
            cMax = 100
            for t in range(len(tmp)):
                if t + cMax <= 100:
                    if find_pelindrome(tmp[t:t+cMax]):
                        flag =1
                        if cMax > long:
                            long = cMax
                        break
                    cMax -= 1
    return long

T = 10
for tc in range(T):
    test = input()
    print(f"#{test} {answer()}")