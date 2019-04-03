import sys
sys.stdin = open('input.txt')


def DFS(k,n):
    if k == M:
        print()




M, N = map(int, input().split())

G = [list(map(int,input().split())) for _ in range(M)]



tmp = []

MAX = 0
DFS(0,0,0,0)
print(MAX)


