import math


def max_heap(A, n, parent):
    largest = parent
    left_child = 2 * parent + 1
    right_child = 2 * parent + 2

    if left_child < n and A[left_child] > A[parent]:
        largest = left_child

    if right_child < n and A[right_child] < A[parent]:
        largest = right_child

    if largest != parent:
        A[largest], A[parent] = A[parent], A[largest]
        max_heap(A, n, largest)


def heap_maximun(A):
    return A[0]


def parent_index(i):
    return math.ceil(i / 2) - 1


def heap_extract_max(A, n):
    max = A[0]
    A[0] = A[n]
    max_heap(A, n - 1, 0)
    return max, A


def heap_increase_key(A, i, key):
    if A[i] > key:
        return 'Key is smaller than A[i]'

    A[i] = key
    while i >= 0 and A[parent_index(i)] < A[i]:
        A[parent_index(i)], A[i] = A[i], A[parent_index(i)]
        i = parent_index(i)

    return A


def max_heap_insert(A, n, key):
    A.append(-9999999)  # -inf
    heap_increase_key(A, n + 1, key)
    return A


A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
print(heap_extract_max(A, len(A) - 1))

A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
print(max_heap_insert(A, len(A) - 1, 10))
