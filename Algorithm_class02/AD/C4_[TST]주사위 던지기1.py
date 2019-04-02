import sys
sys.stdin = open('input.txt')

def perm(k, n):
    global tmp, chk
    if k == n:
        if M == 2:
            ttmp = sorted(tmp)
            if not ttmp in TMP:
                TMP.append(ttmp[::])
                for t in ttmp:
                    print(t, end=' ')
                print()

        else:
            for t in tmp:
                print(t, end=' ')
            print()



    else:
        for i in range(1, 7):
            if M == 3:
                if chk[i] == 0:
                    chk[i] =  1
                    tmp.append(i)
                    perm(k+1,n)
                    tmp.pop()
                    chk[i] = 0

            else:
                tmp.append(i)
                perm(k + 1, n)
                tmp.pop()
TMP = []


N, M = map(int, input().split())
tmp = []
chk = [0]*7
perm(0,N)