def soluteion(data):
    time = 0
    wait = []
    answer = []
    page = 0

    while data or wait:
        # 인쇄중인 것이 없을때

        if data and data[0][1] == time:
            t = data.pop(0)
            wait.append(t)

        if wait:

            if not page:
                wait = sorted(wait, key=lambda x:x[2])
                pre = wait[0][2]
                tmp = [wait[0]]
                for i in range(1,len(wait)):
                    if wait[i][2] != pre:
                        break
                    else:
                        tmp.append(wait[i])

                if len(tmp) == 1:
                    N, T, page = wait.pop(0)
                    answer.append(N)

                else:
                    tmp = sorted(tmp, key=lambda  x:x[0])
                    tN, tT, page = tmp[0]

                    for i in range(len(wait)):
                        if wait[i][0] == tN:
                            wait.pop(i)
                            break
                    answer.append((tN))

            page -= 1

        time+=1

    print(answer)




data = [[1, 99999406, 100000], [2, 99999407, 100000], [3, 99999408, 100000], [4, 99999409, 100000], [5, 99999410, 100000], [6, 99999411, 100000], [7, 99999412, 100000], [8, 99999413, 100000], [9, 99999414, 100000], [10, 99999415, 100000], [11, 99999416, 100000], [12, 99999417, 100000]]
soluteion(data)