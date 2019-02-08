import sys
sys.stdin = open("input.txt")

def binarysearch(num):
    n = 1
    leaf = 0
    for i in range(10):
        if num >= (2**i)-1 and num < 2**(i+1)-1:
            n += (2**(i-1))-1
            if num <= ((2**(i+1)-1)+((2**i)-1))//2:
                n += num - ((2**i)-1)
            else:
                n += 2**(i-1)
            break

    for i in range(10):
        if num >= (2**i)-1 and num < 2**(i+1) - 1:
            if num == (2**i)-1:
                leaf = num
                break
            else:
                leaf = (num - ((2 ** i) - 1)) * 2 - 1
                break



    if num % 2 != 0:
        leaf -= 1
    else:
        leaf += 1


    return n, leaf



T = int(input())


for tc in range(T):
    num = int(input())
    n, k =binarysearch(num)
    print(f'#{tc+1} {n} {k}')