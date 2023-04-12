def max_heap(A, n, parent):
    largest = parent
    left_child = 2 * parent + 1
    right_child = 2 * parent + 2

    if left_child < n and A[left_child] > A[largest]:
        largest = left_child

    if right_child < n and A[right_child] > A[largest]:
        largest = right_child

    if largest != parent:
        A[parent], A[largest] = A[largest], A[parent]
        max_heap(A, n, largest)


def heap_sort(A, n):
    # build max heap
    for i in range(n // 2 - 1, -1, -1):
        max_heap(A, n, i)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heap(A, i, 0)

    return A


A = [15, 3, 99, 1, 25, 7, 9, 9, 1, 100, 6, 1, 0, 12, 4, 2, 9, 0, 87, 122, 54]
print(f'Input: {A}')
heap_sort(A, len(A))
print(A)
