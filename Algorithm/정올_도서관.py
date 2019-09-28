import sys
sys.stdin = open('input.txt')
from queue import PriorityQueue

que = PriorityQueue()
N = int(input())

for _ in range(N):
    s, e = map(int, input().split())
    que.put((s,e))


zero = 0
one = 0

pre_s, pre_e = que.get()


while not que.empty():
    s, e = que.get()
    # 겹치지 않을때
    if pre_e < s:
        if s - pre_e > zero:
            zero = s-pre_e
        pre_s = s
        pre_e = e
    if e-s > one:
        one = e-s

    else:
        if e - pre_s > one:
            one = e-pre_s
            pre_e = e

print(one, zero)