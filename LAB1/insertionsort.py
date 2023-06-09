def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


A = [5, 2, 4, 6, 1, 3]
print(A)
sorted_arr = insertion_sort(A)
print(sorted_arr)
