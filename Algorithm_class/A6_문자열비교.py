import sys
sys.stdin = open("input.txt")
T = int(input())


def find_str(str_y, str_x):

    for x in range(len(str_x)):
        if str_x[x:x+len(str_y)] == str_y:
            return 1
    return 0

for tc in range(T):
    str1 = input()
    str2 = input()
    print(f'#{tc+1} {find_str(str1, str2)}')