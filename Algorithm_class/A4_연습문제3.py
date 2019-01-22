


def find_Min(arr):
    Min = 100
    min_i = 0
    min_j =0
    new_list = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < Min:
                Min = arr[i][j]
                min_i = i
                min_j = j
    arr[min_i][min_j] = 99


    return Min




arr = [[9,20,2,18,11],    # i = 0
       [19,1,25,3,21],
       [8,24,10,17,7],
       [15,4,16,5,6],
       [12,13,22,23,14]]


for _ in range(25):

    print(find_Min(arr))



