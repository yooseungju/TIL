import sys
sys.stdin = open("view.txt")
T = 10



def view_count(l_list):
    cnt = 0
    for i in range(2, len(l_list)-2):
        M = max(l_list[i - 2], l_list[i - 1], l_list[i + 1], l_list[i + 2])
        if (l_list[i]) - M > 0:
            cnt += (l_list[i] - M)

    return cnt






for tc in range(T):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))

    ans = view_count(data)

    print("#{} {}".format(tc+1, ans))