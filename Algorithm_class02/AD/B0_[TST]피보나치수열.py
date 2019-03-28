def fibo(n):
    if n <= 2:
        return 1
    elif M[n-1] != 0:
        if M[n-2] != 0:
            return M[n-1] + M[n-2]
        else:
            return M[n-1] + fibo(n-2)

    else:
        M[n] = (fibo(n-1) + fibo(n-2))
        return M[n]


N = int(input())
M = [0]*(N+1)
print(fibo(N))