import sys
sys.stdin =open('input.txt')

# 버블정렬: n**2시간 복잡도, 원하는 갯수만큼 정렬하고 싶다면 회전수를 정하면됨
def bubbleSort(x):
    #정렬할 대상과 회전수
    for i in range(len(x)-1):
        #비교 대상들
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[i] , x[j]

            # #이차정렬일 경우 안에다가 하나 넣어주면됨
            # if x[i] == x[j]:

#퀵정렬: nlogn , 최악 n**2-절렬이 잘되어 있을경우
# pivot: 기준 , left 비교대상, target:교환할 대상
# 정렬대상의 시작과 끝이 필요
def quickSort(start, end, x):
    if start >= end:
        return
    else:
        pivot = end
        target = start

        for left in range(start, end):
            if x[left] < x[pivot]:
                x[target] , x[left] = x[left], x[target]
                target += 1

        x[target] , x[pivot] = x[pivot], x[target]
        quickSort(start, target-1, x)
        quickSort(target+1, end, x)

# 머지정렬: nlogn, 메모리를 N만큼 필요
def mergeSort(start, end, x):
    if start >= end:
        return
    else:
        mid = (start+end)//2
        mergeSort(start, mid,x)
        mergeSort(mid+1,end, x)

        L, R, T = start, mid+1, start

        while L <= mid and R <=end :
            if x[L] < x[R]:
                tmp[T] = x[L]
                T+=1
                L +=1
            else:
                tmp[T] = x[R]
                T+=1
                R +=1
        while L <= mid:
            tmp[T] = x[L]
            T += 1
            L += 1
        while R <=end:
            tmp[T] = x[R]
            T += 1
            R += 1


N = int(input())
x = list(map(int, input().split()))
quickSort(0,len(x)-1, x)
tmp = [0] * len(x)

for i in x:
    print(i )









