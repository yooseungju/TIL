import sys
sys.stdin = open('input.txt')

cnt = 0

for _ in range(5):
    s, e =map(float, input().split())


    if (e - s) > 1:
        if e-s - 1 < 4:
            cnt += (e-s-1)
        else:
            cnt += 4



if cnt >= 15:
    print( int(cnt*10000*0.95))
elif cnt <= 5:
    print(int(cnt*10000*1.05))

else:
    print(int(cnt*10000))
