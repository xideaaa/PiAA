def bubble_sort(A):
    for i in range(len(A)):
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


A = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(A)
print(A)
