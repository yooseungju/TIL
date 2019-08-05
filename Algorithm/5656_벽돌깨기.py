import sys
sys.stdin = open('input.txt')


def perm(n,w, tmp):
    if n <= 0:
        L.append(tmp[0:])
        
        return

    for i in range(w):
        tmp.append(i)
        perm(n-1, w,tmp)
        tmp.pop()

dy =(-1,1,0,0)
dx =(0,0,-1,1)


def block(i,j,k):
    Q = [(i,j,k)]
    M[i][j] = 0

    while len(Q) > 0:
        x,y,z = Q.pop(0)

        for m in range(4):
            c = z-1
            while c>0:
                nx = x + dx[m]*c
                ny = y + dy[m]*c
                if 0<=nx<H and 0<=ny<W:
                    if M[nx][ny]:
                        Q.append((nx,ny,M[nx][ny]))
                        M[nx][ny] = 0
                c -= 1


def down():
    for w in range(W):
        top = H-1
        for h in range(H-1,-1,-1):
            if M[top][w]:
                top -= 1
            elif M[h][w] and h != top:
                M[top][w] = M[h][w]
                M[h][w] = 0
                top -= 1


def count():
    global MIN
    cnt = 0
    for i in range(H):
        for j in range(W):
            if M[i][j]:
                cnt += 1
    if cnt < MIN:
        MIN = cnt



def throw(case):
    for y in case:
        for x in range(H):
            if M[x][y]:
                block(x,y,M[x][y])
                down()
                break


T = int(input())
for tc in range(T):

    N, W, H = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(H)]
    L =[]

    perm(N,W,[])

    MIN = 0xfffffff

    for i in L:
        M = [D[j][:] for j in range(H)]
        throw(i)
        count()
        if MIN == 0:
            break

    print(f"#{tc+1} {MIN}")

