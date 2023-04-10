A = [2, 4, 5, 1, 11, 10, 31, 6, 16]


def selectionsort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]


selectionsort(A)
print(A)
