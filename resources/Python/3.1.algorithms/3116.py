def min(a):
    ''' Find the least element in a sequence. '''
    minimum = a[0]
    for i in range(1, len(a)):
        if a[i] < minimum:
            minimum = a[i]
    return minimum
