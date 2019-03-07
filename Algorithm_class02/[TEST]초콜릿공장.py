import sys
sys.stdin = open('input.txt')


def overlap(A):
    if len(A) - len(set(A)) > 0:
        return False
    return True



def ans(A, B):
    if overlap(A) and overlap(B):
        if len(set(A)) - len(set(A) - set(B)) > 2  and len(set(B)) - len(set(B) - set(A)) > 2:
            return 0
        else:
            return 1
    else:
        return 1



T = int(input())

SUM = 0
for _ in range(T):
    input_list = input().split()
    A = list(input_list[0])
    B = list(input_list[1])
    SUM += ans(A, B)

print(SUM)