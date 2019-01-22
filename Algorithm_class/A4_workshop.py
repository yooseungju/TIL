import sys
sys.stdin = open("input.txt")


def stick():
    N = int(input())
    arr = list(map(int,input().split()))
    new_arr = []
    start_m = 0

    #첫 값 찾 기
    for index, value in enumerate(arr):
        if arr.count(value)%2==1 and index%2==0:
            start_m = index

    new_arr.append(str(arr[start_m]))
    new_arr.append(str(arr[start_m+1]))

    i = 0

    while i < len(arr):
        if arr[i] == arr[start_m+1]:
            start_m = i
            new_arr.append(str(arr[start_m]))
            new_arr.append(str(arr[start_m + 1]))
            i = 0

        else:
            i += 2

    return ' '.join(new_arr)

T = int(input())

for tc in range(T):
    print(f"#{tc+1} {stick()}")