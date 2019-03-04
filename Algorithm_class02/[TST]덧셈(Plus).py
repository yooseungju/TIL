import sys
sys.stdin = open('input.txt')

A, X = input().split()
flag= 0
for i in range(1,len(A)):
    if int(A[0:1]) + int(A[i:len(A)]) == int(X):
        str = "{} + {} = {}".format(A[0:1],A[i:len(A)],X )
    else:
        str = None
print(str)

