def max_heapify(A, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and A[left_child] > A[largest]:
        largest = left_child

    if right_child < n and A[right_child] > A[largest]:
        largest = right_child

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def build_max_heap(A, n):
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A, n, i)


def heap_sort(A, n):
    build_max_heap(A, n)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A, i, 0)

    return A


A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
heap_sort(A, len(A))
