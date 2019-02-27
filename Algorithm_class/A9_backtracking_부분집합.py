# https://20chally.tistory.com/107?category=732112
arr = [2,3,4]
bit = [0,0,0,0]

k = 0
n = 4


def subset(bit, k, input):
    k += 1
    if k == n:
        print(bit)

    else:
        bit[k] = 0
        subset(bit, k , input)

        bit[k] = 1
        subset(bit, k , input)




subset(bit, k ,n)