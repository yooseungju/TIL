import sys
sys.stdin = open('input.txt')

T = int(input())
def solution():
    global Min
    expect = [[],[]]
    if com_person == [0,0,0,0,0,1]:
        print("d")

    for i in range(len(com_person)):
        # com_person - 0: stair의 첫번째 1:stair의 두번째
        # c - 몇번째 계단인지
        c = com_person[i]
        expect[c].append(abs(stair[c][0]-person[i][0]) + abs(stair[c][1]-person[i][1])+1)

    Max = 0

    for e in range(2):
        hour = 0
        down = []
        length = M[stair[e][0]][stair[e][1]]

        expect[e].sort()

        while expect[e]:
            hour += 1

            while True:
                if down and down[0] == hour:
                    down.pop(0)
                else:
                    break


            while True:
                if expect[e] and len(down)<3 and hour >= expect[e][0]:
                    expect[e].pop(0)
                    # 제일 중요 
                    down.append(hour+length)
                else:
                    break

        if down and Max < down[-1]:
            Max = down[-1]
            
        if Max > Min:
            return

    if Max < Min:
        Min = Max

def com(n,k):
    if n == k:
        solution()
        return

    com_person[n] = 1
    com(n+1,k)

    com_person[n] = 0
    com(n+1,k)


for tc in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]

    stair = []
    person = []

    Min = 0xfffffff

    for i in range(N):
        for j in range(N):
            if M[i][j] > 1:
                stair.append((i,j))

            elif M[i][j] == 1:
                person.append((i,j))



    com_person = [0]*len(person)



    com(0,len(person))

    print("#{} {}".format(tc+1, Min))
