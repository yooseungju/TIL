

a = [[4,2,0],[4,0,3]]

def DFS(n,cnt,i):
    if n == 2:
        return

    for x in range(3):
        if x == i:
