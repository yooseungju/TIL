flag = True
while flag:
    print(flag)

    for j in range(10):
        if j == 6:
            print("똑같아서  break")
            flag = False
            break

    print("for 문 나옴 2" , flag)

    break
