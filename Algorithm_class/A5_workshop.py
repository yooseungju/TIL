import sys
sys.stdin = open("input.txt")
T = int(input())

def cnt(l,s):
    c = 0
    for i in l:
        if i == s:
            c+=1
    return [s]*c

def GNS(Num_list):
    result = []
    for num in ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]:
        result += cnt(Num_list, num)
    return result

for tc in range(T):
    dummy = input()
    Num_list = list(input().split())
    print(f"#{tc+1}\n{' '.join(GNS(Num_list))}")