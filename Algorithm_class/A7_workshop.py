import sys

sys.stdin = open("input.txt")

# sys.stdout = open("output.txt", 'w')





def ans():
    case = int(input())
    size = 100
    M = [list(map(int, input().split())) for _ in range(size)]

    flag = False
    j = 0


    for i in range(99, 0, -1):


        if flag == False:
            j = M[i].index(2)
            flag = True



        else:
            if j < 99 and j > 0:
                #왼쪽
                if M[i][j-1] == 1:
                    for J in range(j-1, -1, -1):
                        if M[i][J] == 0:
                            j = J + 1
                            break

                #오른쪽
                elif M[i][j+1] ==1:
                    if M[i][j + 1] == 1:
                        for J in range(j+1, 100):
                            if M[i][J] == 0:
                                j = J - 1
                                break

            elif j == 0:
                if M[i][j+1] ==1:
                    if M[i][j + 1] == 1:
                        for J in range(j+1, 100):
                            if M[i][J] == 0:
                                j = J - 1
                                break

            elif j == 99:
                if M[i][j-1] == 1:
                    for J in range(j-1, -1, -1):
                        if M[i][J] == 0:
                            j = J + 1
                            break

        print(j)









    for m in M:
        print(m)

    return case , j





for tc in range(10):
    case, a = ans()
    print(f"#{case} {a}")