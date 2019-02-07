import sys
sys.stdin = open("input.txt")

def binarysearch(num):
    n = 1
    k = 1
    for i in range(9):
        if num >= (2**i)-1 and num < 2**(i+1)-1:
            n += (2**(i-1))-1
            if num <= ((2**(i+1)-1)+((2**i)-1))//2:
                n += num - ((2**i)-1)
            else:
                n += 2**(i-1)
            break

    for i in range(9):
        if num >= (2**i)-1 and num < 2**(i+1)-1:
            if num == (2**i)-1:
                k = num
                break
            else:
                k = (num - ((2 ** i) - 1))*2 -1
                break


    if num%2:
        k -= 1
    else:
        k += 1


    return n, k



T = int(input())


for tc in range(T):
    num = int(input())
    n, k =binarysearch(num)
    print(f"#{tc+1} {n} {k}")
