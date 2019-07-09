def extrema(a):
    ''' The extrema from a sequence of integers. '''
    minimum, maximum = a[0], a[0]
    for i in range(1, len(a)):
        if a[i] < minimum:
            minimum = a[i]
        elif a[i] > maximum:
            maximum = a[i]
    return minimum, maximum
