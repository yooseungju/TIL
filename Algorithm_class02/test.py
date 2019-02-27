SIZE = 6
cnt =0

M = [[0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,1,1,1,1,0],
    [0,1,0,0,1,0],
    [0,1,1,1,1,0],
    [0,0,0,0,0,0]]

index = 0
print('   0  1  2  3  4  5')
for i in M:
    print(index, i)
    index +=1

di = [0,0,-1,1]
dj = [-1,1,0,0]

for y in range(SIZE):
    for x in range(SIZE):
        if M[y][x] == 1:
            for m in range(4):
                if y+di[m] >= 0 and y+di[m] < 100 and x+dj[m] >= 0 and x+dj[m] < len(M):

                    if M[y+di[m]][x+dj[m]] == 0:
                        cnt += 1
                        print('cnt:',cnt,y,x)

print(cnt)