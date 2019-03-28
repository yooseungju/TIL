import sys
sys.stdin = open('input.txt')




def BFS(i,j):

    # 좌 우 하 상
    fj = [-1, 1, 0, 0]
    fi = [0, 0, 1, -1]
    # 좌하 좌상 우상 우하 하좌 하우 상좌 상우
    sj = [[-1, -1],[1,1],[-1,1],[-1,1]]
    si = [[1, -1],[-1,1],[1,1],[-1,-1]]
    M[i][j] = 1


    Q = [[i,j]]
    while len(Q)>0:
        q = Q.pop(0)
        for f in range(4):
            if q[0]+fi[f] >= 0 and q[0]+fi[f]<  10 and q[1]+fj[f]>=0 and q[1]+fj[f] < 9:
                if type(M[q[0]+fi[f]][q[1]+fj[f]]) == int:
                    FI = q[0] + fi[f]
                    FJ = q[1] + fj[f]
                    for i in range(2):
                        for s in range(1,3):
                            if s == 1:
                                if FI + si[f][i] * s >= 0 and FI + si[f][i] * s < 10 and FJ + sj[f][i] * s >= 0 and FJ +sj[f][i] * s < 9:
                                    if type(M[FI+si[f][i]*s][FJ + sj[f][i]*s]) != int:
                                        break

                            elif s == 2:
                                if FI + si[f][i] * s >= 0 and FI + si[f][i] * s < 10 and FJ + sj[f][i] * s >= 0 and FJ +sj[f][i] * s < 9:
                                    if M[FI+si[f][i]*s][FJ + sj[f][i]*s] == 0:
                                        M[FI + si[f][i] * s][FJ + sj[f][i] * s] = M[q[0]][q[1]] + 1
                                        Q.append([FI + si[f][i]*s, FJ + sj[f][i] * s])
                                    elif M[FI+si[f][i]*s][FJ + sj[f][i]*s] == 'K':
                                        return M[q[0]][q[1]]


M = [[0]*9 for _ in range(10)]
Si, Sj = map(int, input().split())
Ki, Kj = map(int, input().split())
M[Ki][Kj] = 'K'


print(BFS(Si, Sj))



