def insertion_sort(v):
    len_v = len(v)

    for i in range(1, len_v):
        chave = v[i]
        j = i - 1
        while j >= 0 and v[j] > chave:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave


v = [50, 10, 5, 70, 60, 40]
insertion_sort(v)
print(v)
