

def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

def fibo2(n):
    f = [0,1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

def f(n):
    global factorial
    if n >= len(factorial):
        for i in range(2, n+1):
            factorial.append(factorial[i-1]*i)

    return factorial[n]

factorial = [0,1]


memo = [0,1]

print(f(5))
