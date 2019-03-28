import sys
sys.stdin = open('input.txt')

N = int(input())

M = [list(map(int , list(input()))) for _ in range(N)]
dot = 0
for i in range(N):
    for j in range(N):
        if M[i][j] == 2:
            dot = [i,j]
            break

MAX = 0
max_element = [0,0]
for i in range(N):
    for j in range(N):
        if M[i][j] == 1:
            if MAX < abs(i-dot[0]) + abs(j-dot[1]):
                max_element = [i, j]
                MAX = abs(i-dot[0]) + abs(j-dot[1])

d = (max_element[0]-dot[0])**2 + (max_element[1]-dot[1])**2
print(int(d**0.5+1))

