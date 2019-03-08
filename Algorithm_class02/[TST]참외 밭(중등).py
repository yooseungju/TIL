import sys
sys.stdin = open('input.txt')

n = int(input())

row = []
col = []

for _ in range(6):
    d, l = map(int,input().split())
    if d == 3 or d == 4:
        col.append(l)
    else:
        row.append(l)



ri = row.index(max(row))

ci = col.index(max(col))-2

if ri == 3:
    ri = 0
if ci ==3:
    ci = 0



print(row)
print(col)

print(ri)
print(ci)

print(n*((max(row)*max(col)-(row[ri]*col[ci]))))