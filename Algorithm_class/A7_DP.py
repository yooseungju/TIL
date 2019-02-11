

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



memo = [0,1]

print(fibo1(5))
print(fibo2(5))