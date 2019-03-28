

P = list(input())




pre = ''
ans = 0
for p in P:
    if pre == '':
        ans += 10
        pre = p

    else:
        if pre == p:
            ans += 5
        else:
            ans += 10
        pre = p


print(ans)




