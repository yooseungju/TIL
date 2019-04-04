
import sys
sys.stdin = open('input.txt')



def BFS():
    # 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4
    dj = (0,1,-1,0,0)
    di = (0,0,0,1,-1)
    turn = [(0,0),(),(),()]

    Q=[(rx,ry,rd,cnt)]







# 세로 가로
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
chk = [[[0]*4 for _ in range(N)] for _ in range(M)]
print(chk)
rx, ry, rd =  map(int, input().split())
dx, dy, dd =  map(int, input().split())
cnt = 0
