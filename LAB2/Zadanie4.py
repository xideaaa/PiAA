#quicksort stabilny
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    l, q, r = [], [], []
    for item in arr:
        if item < arr[0]:
            l.append(item)
        elif item > arr[0]:
            r.append(item)
        else:
            q.append(item)
    sub = quicksort(l) + q + quicksort(r)
    print(*sub)
    return sub


n = input().strip().split()
ar = [int(x) for x in input().strip().split()]
quicksort(ar)

"""
def quicksort(A, left, right):
    if left < right:
        p = partition(A, left, right)
        quicksort(A, left, p - 1)
        quicksort(A, p + 1, right)

def partition(A, left, right):
    pivot = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    
    # Przesuń elementy o takiej samej wartości jak pivot na początek partycji
    j = i
    for k in range(i - 1, left - 1, -1):
        if A[k] == A[i + 1]:
            A[k], A[j] = A[j], A[k]
            j -= 1
    
    return i + 1
"""
