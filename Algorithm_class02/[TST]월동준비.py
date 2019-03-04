import sys
sys.stdin = open('input.txt')

N = int(input())
l = list(map(int, input().split()))


def fasttenstMaxsum(arr):
    global N
    ret = 0
    psum = 0

    for i in range(N):
        psum = max(psum,0) + arr[i]
        ret = max(psum, ret)
    return ret

print(fasttenstMaxsum(l))