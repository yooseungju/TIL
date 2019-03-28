import sys
import time
sys.stdin = open('input.txt')

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


def cnt(first,second):
    global count
    flag = 0
    for k in input_list[second+1:N]:
        if k-input_list[second] <= (input_list[second] - input_list[first])*2:
            if input_list[second] - input_list[first] <= k-input_list[second]:
                count += 1

        else:
            break

N = int(input())
input_list = merge_sort([int(input()) for _ in range(N)])
count = 0

for i in range(N-1):
    for j in range(i+1,N-1):
        cnt(i, j)
print(count)

