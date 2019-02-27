import sys
sys.stdin = open('input.txt')

A = 300
B = 60
C = 10

T = int(input())



def pprint(T):
    A = 300
    B = 60
    C = 10
    a_mod = T // A
    for a in range(a_mod,-1,-1):
        aa = T - (a*A)
        b_mod = aa // B
        for b in range(b_mod, -1,-1):
            c = aa - (b*B)
            if c % C == 0:
                return print(a, b, c//C)


    return print(-1)
pprint(T)

