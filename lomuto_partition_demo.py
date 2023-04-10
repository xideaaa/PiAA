A = [2, 4, 5, 1, 11, 10, 31, 6, 16, 8]


def partition(A, left, right):
    pivot = A[right]
    i = left - 1
    print(f'START: i={i}, j={left}, pivot={pivot}, left={left}, right={right}')
    for j in range(left, right):
        print(f'{A}; i={i}, j={j}, pivot={pivot}, left={left}, right={right}')
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    print(f'{A}; i={i}, j={j}, pivot={pivot}, left={left}, right={right}')
    print(f'RET {i+1}')
    return i + 1


def quicksort(A, left, right):
    if left < right:
        q = partition(A, left, right)


quicksort(A, 0, len(A) - 1)
