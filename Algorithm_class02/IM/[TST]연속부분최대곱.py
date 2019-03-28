import sys
sys.stdin = open('input.txt')

def n():
    l = []
    N = int(input())

    for _ in range(N):
        t = float(input())
        if l == []:
            l.append(t)
        elif l[-1]*t > t:
            l.append(l[-1]*t)
        else:
            l.append(t)
    print(l)

    return max(l)

print('%0.3f'%n())
