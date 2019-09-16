import sys
sys.stdin = open('input.txt')
T = int(input())

def down():
    global MIN,s


    waite = [[],[]]
    for i in range(s):
        x1, y1 = person[i]
        x2, y2 = stair[tmp[i]]
        waite[tmp[i]].append(abs(x1-x2)+abs(y1-y2)+1)

    per_time = [0,0]

    for st in range(2):

        fill = []
        waite[st].sort()
        second = 0

        while waite[st]:
            second += 1

            while 1:
                if fill and fill[0] == second:
                    fill.pop(0)
                else:
                    break

            while 1:
                if waite[st] and waite[st][0] <= second and len(fill) < 3:
                    waite[st].pop(0)
                    fill.append(second+stair_time[st])
                else:
                    break


        if fill:
            per_time[st] = fill[-1]



    if MIN > max(per_time):
        MIN = max(per_time)

def com(n):
    if n == s:
        down()
        return

    tmp[n] = 1
    com(n+1)
    tmp[n] = 0
    com(n+1)


for tc in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]

    person = []
    stair = []
    stair_time = []

    for i in range(N):
        for j in range(N):
            if M[i][j] == 1:
                person.append((i,j))
            elif M[i][j] > 1:
                stair.append((i,j))
                stair_time.append(M[i][j])

    MIN = 0xfffffff

    s = len(person)
    tmp = [0]*s
    com(0)

    print("#{} {}".format(tc+1, MIN))





