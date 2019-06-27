def largest_even(a):
    ''' Find the largest even list entry. '''
    index = None
    for i in range(len(a)):
        if not a[i] % 2:
            if (not index) or (a[i] > a[index]):
                index = i
    return index 