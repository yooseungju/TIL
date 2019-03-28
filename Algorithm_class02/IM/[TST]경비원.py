import sys
sys.stdin  = open('input.txt')

w , h = map(int,input().split())
N = int(input())
M = []
for _ in range(N+1):
    d , offset = map(int, input().split())
    dot = []
    if d == 1:
        dot = [offset, h]
    elif d == 2:
        dot = [offset, 0]
    elif d == 3:
        dot = [0, h-offset]
    elif d == 4:
        dot = [w, h-offset]
    M.append(dot)

for m in range(N):


