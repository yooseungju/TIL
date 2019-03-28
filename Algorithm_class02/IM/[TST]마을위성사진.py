import sys
sys.stdin = open('input.txt')


T = int(input())

M = [list(map(int, list(input()))) for _ in range(T)]
len(M)


di = [0,0,-1,1]
dj = [-1,1,0,0]

Max = 0
l =1

while l < T-l:
    for i in range(l, T-l):
        for j in range(l, T-l):
            Min = 1000
            flag = 1
            if i == l and j != l and i != T-l-1 and j != T-l-1:
                break
            if M[i][j] != 0:
                for m in range(4):
                    if 0 <= i+di[m] < T and 0 <= j+dj[m] < T:
                        if M[i+di[m]][j+dj[m]] != 0:
                            if Min > M[i+di[m]][j+dj[m]]:
                                Min = M[i+di[m]][j+dj[m]]
                        else:
                            flag = 0 #사방탐색하다가 0인게 있으면
                            break
                if flag == 1:
                    M[i][j] = Min + 1
                if Max < M[i][j]:
                    Max = M[i][j]
    l += 1
print(Max)
