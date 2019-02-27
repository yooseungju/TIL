N , n = map(int , input().split())

M = [list(map(int, input().split())) for _ in range(N)]

pre = ''
for i in range(N):
    for j in range(n):
        if pre == '':
            pre = M[i][j]
        else:
            if M[i][j] == 1:
                if pre > 0:
                    M[i][j] = pre+1
                    pre = M[i][j]
                else:
                    pre = M[i][j]
            else:
                pre = M[i][j]
        print(M[i][j] , end=' ')
    pre = ''
    print()