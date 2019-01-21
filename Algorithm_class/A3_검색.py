def sequentialSearch(a, key):
    n = len(a)
    i = 0
    while i < n and a[i] !=key:
        i += 1
    if i< n : return i
    else: return -1


def binarySearch(a,key):
    start = 0
    end = len(a)-1

    while start <= end:
        middle = (start+end)//2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else: start = middle +1
    return False

#선택 정렬
def select(l,k):
    for i in range(0,k):
        minIndex = i
        for j in range(i+1, len(l)):
            if l[minIndex] > l[j]:
                minIndex = j
        l[i], l[minIndex] = l[minIndex], l[i]
    return l[k-1]


# print(sequentialSearch([5,2,6,4,1,8,7,9,3], 8))
# print(binarySearch([1,2,3,4,5,6,7,8] ,5))