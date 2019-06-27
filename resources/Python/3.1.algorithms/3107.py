def last_even(a):
    ''' Find the last even list entry. '''
    index = None
    for i in range(len(a)):
        if not a[i] % 2:
            index = i
    return index