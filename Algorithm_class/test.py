def win(x,y):
    if x + 1 == y or(x == 3 and y ==1):
        return y
    else:
        return x


x, y = map(int,input().split())

print(win(x, y))