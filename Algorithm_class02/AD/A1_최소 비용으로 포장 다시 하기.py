import sys
sys.stdin = open('input.txt')



def bubbleSort(start):
    for i in range(start, start+2):
        for j in range(i+1 , len(dummy)):
            if dummy[i] > dummy[j]:
                dummy[i], dummy[j] = dummy[j], dummy[i]




SUM = 0
N = int(input())
dummy = list(map(int, input().split()))
start = 0

while start < len(dummy)-1:
    bubbleSort(start)
    start += 1
    dummy[start] = sum(dummy[start-1:start+1])
    SUM += dummy[start]

print(SUM)


