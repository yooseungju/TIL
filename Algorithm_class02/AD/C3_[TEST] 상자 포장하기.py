import sys
sys.stdin = open('input.txt')

def DFS(no, Apre, Bpre, Sum):
    global MAX

    if no == N:
        if Sum > MAX:
            MAX = Sum
        return

    else:
        if box[no] < Apre:
            DFS(no+1, box[no], Bpre, Sum + box[no])
        if box[no] > Bpre:
            DFS(no + 1, Apre, box[no], Sum + box[no])
        DFS(no + 1, Apre, Bpre, Sum)

T = int(input())
for _ in range(T):
    MAX = 0
    N = int(input())
    box = list(map(int, input().split()))
    DFS(0, 1000, 0, 0)
    print(MAX)