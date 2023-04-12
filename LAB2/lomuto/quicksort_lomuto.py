A = [2, 4, 5, 1, 11, 10, 31, 6, 16, 3]


def partition(A, left, right):
    pivot = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1


def quicksort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quicksort(A, left, q - 1)
        quicksort(A, q + 1, right)


quicksort(A, 0, len(A)-1)
print(A)
