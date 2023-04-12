def bucket_sort(arr):
    # Określ maksymalną wartość w tablicy wejściowej
    max_val = max(arr)
    # Utwórz kubełki w zależności od maksymalnej wartości
    buckets = [list() for _ in range(max_val + 1)]
    # Przypisz każdą wartość z tablicy wejściowej do odpowiadającego jej kubełka
    for val in arr:
        buckets[val].append(val)
    # Sortuj każdy kubełek za pomocą sortowania przez wstawianie
    for bucket in buckets:
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key
    # Zwróć posortowaną tablicę
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += bucket
    return sorted_arr