def max_difference(a):
    ''' Max adjacent list entry difference. '''
    maximum = 0
    for i in range(1, len(a)):
        difference = a[i] - a[i-1]
        if maximum < difference:
            maximum = difference
    return maximum
