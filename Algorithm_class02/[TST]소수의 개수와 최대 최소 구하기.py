import sys
sys.stdin = open('input.txt')


def primes_up_to_good(n:int) -> [int]:
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5):
        if seive[k]: seive[k*2::k] = [False] * ((n - k) // k)
    return [x for x in range(n+1) if seive[x]]




