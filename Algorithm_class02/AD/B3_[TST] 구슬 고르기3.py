def perm(k, n):

    if n == k:
        for t in T:
            print(t, end=' ')
        print()
        return

    for i in arr:
        if not chk[i]:
            chk[i] = 1
            T[k] = i
            perm(k+1, N)
            T[k] = i
            chk[i] = 0


T = [0] *3
N = 3
chk = [0] * (N+1)
arr = [ i for i in range(1,4)]
perm(0, N)