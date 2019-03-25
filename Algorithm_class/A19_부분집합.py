count = 0
N = 1
A = [0 for _ in range(N)]

data = [1,2,3,4,5,6,7,8,9,10]
total = 0
def printSet(n):
    global count
    count += 1
    print("%d: " % (count), end="")
    for i in range(n):
        if A[i] == 1:
            print("%d " % data[i], end='')
    print()

def powerset(n,k, sum):
    global total
    if sum > 10:
        return
    if n == k:
        if sum == 10:
            printSet(n)
    else:
        total += 1
        A[k] = 1
        powerset(n,k+1, sum+data[k])
        A[k] = 0
        powerset(n, k+1, sum)

powerset(N,0, 0)
print(total)