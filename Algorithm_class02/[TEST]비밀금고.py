import sys
sys.stdin =  open('input.txt')

N = int(input())
num = list(map(int, input().split()))


for i in range(N*2-1):
    for j in range(N*2-1):
        if j *2 == N+1:
            print('*', end = ' ')
        else:
            print(0, end = ' ')
        N -= 1

    print()



