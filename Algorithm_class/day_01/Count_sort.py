def Count_sort(A):

    k = max(A)
    B = [0] * len(A)
    C = [0] * (k+1)



    for i in A:
        C[i] += 1


    for i in range(1, len(C)):
        C[i] += C[i-1]


    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    print(B)




Count_sort([1,0,4,5,8,2,4,9,1,4,5])
