import sys
sys.stdin = open("input.txt")



def dfs(N, s, I):
    global Max
    if N <= 0:
        s = int(''.join(map(str,s)))
        if Max < s:
            Max = s
        return


    for i in range(I, size):
        for j in range(i + 1, size):
            if s[j] >= s[i]:
                tmp =[i for i in s]
                tmp[i], tmp[j] = tmp[j], tmp[i]
                dfs(N-1,tmp,i)




T = int(input())
for tc in range(T):
    S, N = input().split()

    N = int(N)
    S = list(map(int, list(S)))
    size = len(S)
    Max = 0
    dfs(N, S, 0)
    print(f"{tc+1} {Max}")