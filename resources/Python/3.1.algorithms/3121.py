def partial_sort(a):
    ''' Sort the first 3 terms in a. '''
    for i in range(2):
        for j in range(2 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
