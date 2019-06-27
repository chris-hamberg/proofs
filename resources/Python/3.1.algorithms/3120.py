def extrema(a):
    minimum, maximum = a[0], a[0]
    for i in range(1, len(a)):
        if a[i] < minimum:
            minimum = a[i]
        if a[i] > maximum:
            maximum = a[i]
    return minimum, maximum
