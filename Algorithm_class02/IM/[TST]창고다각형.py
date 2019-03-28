import sys
sys.stdin = open('input.txt')

SIZE = 1001
N =  int(input())


roof = [0] * SIZE
Max = 0
Max_idx = 0
for _ in range(N):
    L , H = map(int, input().split())
    roof[L] = H
    if Max < H:
        Max = H
        Max_idx = L

area = 0
index = 0
pre = 0

while index < Max_idx:
    if roof[index] > pre:
        pre = roof[index]
    area += pre
    index += 1



index= SIZE -1
pre = 0
while index >= Max_idx:
    if roof[index] > pre:
        pre = roof[index]
    area += pre
    index -= 1

print(area)















