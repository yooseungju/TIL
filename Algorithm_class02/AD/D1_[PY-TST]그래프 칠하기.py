import sys
sys.stdin = open('input.txt')

def check(no, color):
    for i in range(no):
        if arr[no][i] and rec[i] == color:
                return True
    return False

def DFS(no):
    global flag
    if 0 not in rec:
        flag = 1
        return
    for c in range(1,M+1):
        if not check(no, c):
            rec[no] = c
            DFS(no+1)
            if not flag:
                rec[no] = 0
            else: return
# main---------------------------------------------------------------------
N, M = map(int, input().split())
rec= [0]*N
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

flag = 0
DFS(0)
if flag:
    for i in range(N):
        print(rec[i], end=' ')
else:print(-1)

print()
