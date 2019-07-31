import sys
sys.stdin = open("input.txt")



def DFS(s):
    global ans
    if ans:
        return
    if s==99:
        ans = 1
        return


    for i in range(100):
        if M[s][i] == 1:
            DFS(i)



for tc in range(10):
    N, E = map(int, input().split())

    M = [[0]*100 for i in range(100)]

    tmp = list(map(int, input().split()))

    ans = 0
    for i in range(0, E*2, 2):
        M[tmp[i]][tmp[i+1]] = 1


    DFS(0)
    print(f"#{tc+1} {ans}")


