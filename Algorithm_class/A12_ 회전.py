import sys
sys.stdin = open('회전_input.txt')
T = int(input())


for tc in range(T):
    N, M = map(int, input().split())
    num_list = input().split()
    mod = M % N
    front = 0
    rear = N
    for _ in range(mod):
        front = (front + 1) % N


    print(f'#{tc+1} {num_list[front]}')

