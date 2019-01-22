import sys
sys.stdin = open("input.txt")


T = int(input())

def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]



def s_sort():
    N = input()
    arr = list(map(int, input().split()))
    selectionSort(arr)


    new_arr = []
    pivot = len(arr)//2
    j = 0

    for i in arr[0:pivot]:
        new_arr.append(str(arr[len(arr)-1+j]))
        new_arr.append(str(i))
        j -= 1

    result  = ' '.join(new_arr[:10])
    return result




for tc in range(T):
    print(f"#{tc+1} {s_sort()}")