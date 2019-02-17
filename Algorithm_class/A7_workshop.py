import sys
sys.stdin = open("input.txt")

<<<<<<< HEAD

def ans():
    case = int(input())
    size = 100
    M = [list(map(int, input().split())) for _ in range(size)]

    j = M[99].index(2)

    for i in range(98, 0, -1):
        if j < 99 and j > 0:
            if M[i][j - 1] == 1:
                for J in range(j - 1, -1, -1):
                    if M[i][J] == 0:
                        j = J + 1
                        break
                    j =  0


            elif M[i][j + 1] == 1:
                if M[i][j + 1] == 1:
                    for J in range(j + 1, 100):
                        if M[i][J] == 0:
                            j = J - 1
                            break
                        j = 99


        elif j == 0:
            if M[i][j + 1] == 1:
                if M[i][j + 1] == 1:
                    for J in range(j + 1, 100):
                        if M[i][J] == 0:
                            j = J - 1
                            break

        elif j == 99:
            if M[i][j - 1] == 1:
                for J in range(j - 1, -1, -1):
                    if M[i][J] == 0:
                        j = J + 1
                        break
    return case, j

for tc in range(10):
    case, a = ans()
    print(f"#{case} {a}")
=======
for tc in range(1, 11):
   dummy = int(input())
   data = [list(map(int, (input().split()))) for i in range(100)]

   y = 99
   x = data[99].index(2)

   while y > 0:
       y -= 1
        # 오른쪽에 1이 있으면
       if x < 99 and data[y][x + 1] == 1:
           x += 1
           #위가 1이 나올때 까지
           while data[y-1][x] != 1:
               x += 1

       elif x > 0 and data[y][x - 1] == 1:
           x -= 1
           while data[y-1][x] != 1:
               x -= 1

       elif y == 0:
           print("#{} {}".format(tc, x))
>>>>>>> 7cbd1e3716a15e0dbef1006fe14c59b7d4f0f93f
