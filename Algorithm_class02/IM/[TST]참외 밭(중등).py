import sys
sys.stdin = open('input.txt')

n = int(input())

direction = []
length = []

for _ in range(6):
    d, w = map(int, input().split())
    direction.append(d)
    length.append(w)

direction *= 2
length *= 2

h = [[1,3],[4,3],[2,4],[3,2]]

for i in range(len(direction)):
    if direction[i:i+2] in h:
        small = length[i] * length[i+1]
        big1 = length[i+3]
        big2 = length[i+4]
        print(n*(big1*big2-small))
        break