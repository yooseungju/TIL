import sys
sys.stdin = open('input.txt')

T = int(input())

def code(i, j):
    global CODE

    ans = []
    code_list = [[0,0,0,1,1,0,1],
                 [0,0,1,1,0,0,1],
                 [0,0,1,0,0,1,1],
                 [0,1,1,1,1,0,1],
                 [0,1,0,0,0,1,1],
                 [0,1,1,0,0,0,1],
                 [0,1,0,1,1,1,1],
                 [0,1,1,1,0,1,1],
                 [0,1,1,0,1,1,1],
                 [0,0,0,1,0,1,1]]

    cnt = 8

    while cnt > 0:
        ans.append(CODE[i][j:j+7])
        j += 7
        cnt -= 1

    even = 0
    odd = 0
    for a in range(8):
        if a == 7:
            if ((odd *3) + even + code_list.index(ans[7])) % 10 == 0:
                return odd + even + code_list.index(ans[7])
            else:
                return 0
        elif a % 2 == 0:
            odd += code_list.index(ans[a])
        else:
            even += code_list.index(ans[a])



for tc in range(T):
    N, M = map(int, input().split())

    CODE = [list(map(int, list(input()))) for _ in range(N)]
    flag = 1

    A = 0
    for i in range(N):
        if flag:
            for j in range(M-1, -1, -1):
                if CODE[i][j] == 1:
                    A = code(i, j-55)
                    flag = 0
                    break
        else: break

    print("#{} {}".format(tc+1, A))

