A = [2, 4, 5, 1, 11, 10, 31, 6, 16, 3]


def partition(A, left, right):
    pivot = A[left]
    i = left
    j = right
    while True:
        while A[i] > pivot:
            i += 1
        while A[j] < pivot:
            j -= 1
        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]


def quicksort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quicksort(A, left, q)
        quicksort(A, q + 1, right)


quicksort(A, 0, len(A) - 1)
print(A)
