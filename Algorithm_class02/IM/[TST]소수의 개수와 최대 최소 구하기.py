import sys
sys.stdin = open('input.txt')

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 is 0 or n % 3 is 0:
        return False
    if n < 9:
        return True
    k, l = 5, n**0.5
    while k <= l:
        if n % k is 0 or n % (k+2) is 0:
            return False
        k += 6
    return True


a, b = map(int, input().split())
A = min(a,b)
B = max(a,b)

prime_min = False
prime_max = False
cnt = 0

for i in range(A, B+1):
    if is_prime(i):
        cnt += 1
        if not prime_min and not prime_max:
            prime_max = i
            prime_min = i
        else:
            if i > prime_max:
                prime_max = i
            if i < prime_min:
                prime_min = i
print(cnt)
print(prime_min+prime_max)





