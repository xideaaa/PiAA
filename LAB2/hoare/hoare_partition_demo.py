A = [2, 4, 5, 1, 11, 10, 31, 6, 16, 8]


def partition(A, left, right):
    pivot = A[left]
    i = left
    j = right
    print(f'START: i={i}, j={j}, pivot={pivot}, left={left}, right={right}')
    while True:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        print(f'{A}; i={i}, j={j}, pivot={pivot}, left={left}, right={right}')
        if i >= j:
            print(f'RET {j}')
            return j
        A[i], A[j] = A[j], A[i]
        print(f'SWAP: {A}; i={i}, j={j}, pivot={pivot}, left={left}, right={right}')


partition(A, 0, len(A) - 1)
