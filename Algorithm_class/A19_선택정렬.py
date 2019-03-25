def SelectionSort(A, s, e):
    mini = s
    if s == e:
        return
    for j in range(s+1,e,1):
        if A[j] < A[mini]:
            mini = j

    A[mini], A[s] = A[s], A[mini]
    SelectionSort(A, s+1,e)



A = [9, 6, 7, 3, 5]
n = len(A)
print(SelectionSort(A, 0, len(A)-1))

