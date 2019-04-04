import sys
sys.stdin = open('input.txt')

def DFS(k, SUM):
    global MIN
    if 0 not in vistied:
        if M[k][0] > 0 and SUM+M[k][0] < MIN:
            MIN = SUM+M[k][0]
        return

    for s in range(N):
        if M[k][s]  != 0 and vistied[s] == 0:
            vistied[s] = 1
            DFS(s, SUM+M[k][s])
            vistied[s] = 0


# def DFS(k, SUM):
#     global MIN
#     if 0 not in vistied:
#         if M[k][0] > 0 and SUM+M[k][0] < MIN:
#             MIN = SUM+M[k][0]
#
#
#
#     for s in range(1,N):
#         if M[k][s] != 0 and not vistied[s]:
#             vistied[s] = 1
#             DFS(s, SUM+M[k][s])
#             vistied[s] = 0


N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
vistied =  [0]*N
vistied[0] =1
MIN = 0xfffffff
DFS(0,0)
print(MIN)



