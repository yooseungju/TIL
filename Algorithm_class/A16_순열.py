def pyprint(q):
    while(q):
        q -= 1
        print(" %d" % (t[q]), end='')

    print()

def perm(n,r,q):
    if r ==0:
        myprint(q)