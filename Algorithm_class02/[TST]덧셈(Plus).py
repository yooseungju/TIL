import sys
sys.stdin = open('input.txt')

A, X = input().split()
str  =  "NONE"
for i in range(1,len(A)):
    if int(A[0:i])+int(A[i:len(A)])==int(X):
        str = "{}+{}={}".format(int(A[0:i]),int(A[i:len(A)]),X )
        break
print(str)

