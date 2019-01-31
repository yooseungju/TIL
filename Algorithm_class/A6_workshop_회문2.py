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


    # 가로 세로 함께 탐색
    for i in range(100):
        length = 100 #100길이 부터 펠린드롬이 있는지 확인
        flag = 0
        # 회문을 찾지 않았고 탐색 길이가 찾아진 길이 보다 길때만 탐색
        while flag == 0 and length > long:
            for j in range(100):
                if j + length <= 100 :
                    if find_pelindrome(arr[i][j:j+length]) or find_pelindrome([arr[v][i] for v in range(j,j+length)]):
                        flag = 1
                        if long < length:
                            long = length
                        break
                else:
                    length -= 1
                    break
    return long

T = 10
for tc in range(T):
    test = input()
    print(f"#{test} {answer()}")