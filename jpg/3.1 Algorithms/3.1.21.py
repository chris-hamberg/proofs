def partial_sort(a):
    for i in range(2):
        for j in range(2):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
