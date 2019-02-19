import sys
sys.stdin = open('input_토너먼트.txt')

T = int(input())



def ans():
    global L
    size = int(input())
    L = list(map(int, input().split()))
    return tournament(0, len(L)-1)+1



def win(x,y):
    if L[x] + 1 == L[y] or(L[x] == 3 and L[y] ==1):
        return y
    else:
        return x


def tournament(start , end):
    global L
    if end == start:
        return start
    elif end-start == 1:
        return win(start,end)
    else:
        middle = (start+end)//2
        return(win(tournament(start, middle), tournament(middle+1,end)))




for tc in range(T):
    print(f'#{tc+1} {ans()}')