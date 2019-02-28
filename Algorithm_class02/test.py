
for j in range(10):
    for i in range(10):
        if i == 5:
            continue
        if i == 6:
            break
    print(j, 'break 나옴')