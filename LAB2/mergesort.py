A = [2, 4, 5, 1, 11, 10, 31, 6, 16]


def merge(A, left, mid, right):
    L = A[left:mid+1]
    R = A[mid+1:right+1]

    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


def mergesort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        mergesort(A, left, mid)
        mergesort(A, mid + 1, right)
        merge(A, left, mid, right)


mergesort(A, 0, len(A) - 1)