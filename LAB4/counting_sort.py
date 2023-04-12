def counting_sort(arr):
    n = len(arr)
    k = max(arr) + 1
    counts = [0] * k
    result = [0] * n

    # zliczanie wystąpień elementów
    for i in range(n):
        counts[arr[i]] += 1

    print(counts)
    # obliczanie pozycji w tablicy wynikowej
    for i in range(1, k):
        counts[i] += counts[i - 1]
    print(counts)
    # umieszczanie elementów w tablicy wynikowej
    for i in range(n - 1, -1, -1):
        result[counts[arr[i]] - 1] = arr[i]
        print(result)
        counts[arr[i]] -= 1

    return print(result)

A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
counting_sort(A)