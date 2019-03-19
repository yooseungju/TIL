import sys
sys.stdin = open('input.txt')


T = int(input())


def code_number(bin_arr,p):


    true_code = []

    num_dict = [[3, 2, 1, 1],
                [2, 2, 2, 1],
                [2, 1, 2, 2],
                [1, 4, 1, 1],
                [1, 1, 3, 2],
                [1, 2, 3, 1],
                [1, 1, 1, 4],
                [1, 3, 1, 2],
                [1, 2, 1, 3],
                [3, 1, 1, 2]
                ]

    for bin_numbers in bin_arr:
        tmp = []
        pre = '0'
        cnt = 1

        for index, b in enumerate(bin_numbers[1::],1):
            if index == (7*p)-1:
                if b == pre:
                    cnt += 1
                else:
                    tmp.append(cnt)
                    cnt = 1
                tmp.append(cnt)
                break
            if b == pre:
                cnt+=1
            else:
                tmp.append(cnt)
                cnt = 1
            pre = b



        for f in range(4):
            tmp[f] //= p
        true_code.append(num_dict.index(tmp))



    even = 0
    odd = 0


    for a in range(8):
        if a == 7:
            if ((odd * 3) + even + true_code[a]) % 10 == 0:
                return odd + even + true_code[-1]
            else:
                return 0
        elif a % 2 == 0:
            odd += true_code[a]
        else:
            even += true_code[a]



def my_bin(a):
    str_bin = ''

    for h in a:
        b = format(int('0x'+h , 16), 'b')
        if len(b) < 4:
            b = '0'*(4-len(b)) + b
        str_bin += b


    for o in range(len(str_bin)-1,-1,-1):
        if str_bin[o] != '0':
            str_bin = str_bin[0:o+1]
            break


    if len(str_bin) > 56:
        proportion = len(str_bin) // 56
    else:
        proportion = 1

    s = len(str_bin)-1
    bin_arr = []
    len_code = 8

    while len_code > 0:
        if len(str_bin[0:s+1]) < (7*proportion):
            bin_arr.insert(0,'0'*(7*proportion-len(str_bin[0:s+1]))+str_bin[0:s+1])
        else:
            bin_arr.insert(0, str_bin[s - (7 * proportion) + 1:s + 1])
        s = s-(7*proportion)

        len_code -= 1

    print(a)
    print(str_bin)
    print(bin_arr)

    return code_number(bin_arr, proportion)


def solution():
    global N, M, arr, cnt

    for i in range(N):
        flag = 0
        a = []
        j = M-1
        while j > 0:
            if arr[i][j] != '0' and (i-1 < 0 or arr[i-1][j] == '0'):
                a = arr[i][0:j+1]
                flag = 1

            if flag:
                cnt += my_bin(a)
                flag = 0
                break
            j -= 1

for tc in range(T):
    IN = input().split()
    N = int(IN[0])
    M = int(IN[1])
    cnt = 0
    arr = [list(input()) for _ in range(N)]
    solution()
    print('#{} {}'.format(tc+1, cnt))