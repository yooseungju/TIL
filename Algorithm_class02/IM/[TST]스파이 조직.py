import sys
sys.stdin = open('input.txt')
Input = input().split()

N = int(Input[0])
List = Input[1]
M = []
pre = 0

for j in range(len(List)):
    if List[j].isdigit():
        if pre == 1:
            M[-1] = M[-1]+List[j]
        else:
            M.append(List[j])
        pre = 1
    else:
        M.append(List[j])
        pre = 0


D = {x:[] for x in range(51)}
first = M[0]

def ans(List):
    global first
    a = 0
    while List[-1] != first:
        s = List.pop(-1)
        if s == "<":
            a += 1
        elif s ==">":
            a -=1
    return a

for i in range(1, len(M)):
    if M[i].isdigit():
        D[ans(M[0:i+1][:])].append(M[i])

print(' '.join(D[N]))
