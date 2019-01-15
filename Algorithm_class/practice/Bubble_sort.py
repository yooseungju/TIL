def BubbleSorte(a):
    for i in range(len(a)-1 , 0 , -1): # 4,3,2,1
        for j in range(0, i): # 4번 3번 2번 1번
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] # swap

    print(a)



l_list = list(map(int, input().split(' ')))
BubbleSorte(l_list)

